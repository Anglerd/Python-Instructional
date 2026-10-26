import db_connector
try:
    from flask import Flask, request, jsonify
except ImportError:
    print("Flask not found. Installing...")
    db_connector.install_package("flask")
    from flask import Flask, request, jsonify
try:
    from flask_cors import CORS
except ImportError:
    print("flask-cors not found. Installing...")
    db_connector.install_package("flask-cors")
    from flask_cors import CORS
# ----------------------

import game_logic

app = Flask(__name__)
CORS(app)   # <-- ENABLE CORS FOR ALL ROUTES
# ------------------- Helper: convert your 8x8 board to a dict for JSON -------------------
def board_to_json(board_2d):
    """Turn the 2D array of game_piece objects into a simple 8x8 array of short strings."""
    grid = []
    for row in board_2d:
        r = []
        for piece in row:
            if piece is None:
                r.append(None)
            else:
                # Convert to a format like 'wP' (white pawn) or 'bK' (black king)
                color_char = 'w' if piece.color == 1 else 'b'
                piece_char = {
                    'king': 'K', 'queen': 'Q', 'rook': 'R',
                    'bishop': 'B', 'knight': 'N', 'pawn': 'P'
                }[piece.type]
                r.append(color_char + piece_char)
        grid.append(r)
    return grid

# ------------------- API endpoints -------------------


@app.route('/api/new_game', methods=['POST'])
def new_game():
    data = request.get_json()
    white_id = data.get('white_id')
    black_id = data.get('black_id')
    if not white_id or not black_id:
        return jsonify({'error': 'white_id and black_id required'}), 400

    try:
        board_id = game_logic.start_board(white_id, black_id)
    except Exception as e:
        return jsonify({'error': f'Database error: {str(e)}'}), 500

    return jsonify({'board_id': board_id})


@app.route('/api/load_game/<int:board_id>')
def load_game(board_id):
    board_data = game_logic.load_board(board_id)
    if board_data is None:
        return jsonify({'error': 'Game not found'}), 404

    return jsonify({
        'board_id': board_data['board_id'],
        'white_player': board_data['white_player'],
        'black_player': board_data['black_player'],
        'turn': 'white' if board_data['turn_id'] == board_data['white_player'] else 'black',
        'check_state': board_data['check_state'],
        'board': board_to_json(board_data['board'])
    })


@app.route('/api/move', methods=['POST'])
def make_move():
    data = request.get_json()
    board_id = data.get('board_id')
    from_row = int(data.get('from_row'))
    from_col = int(data.get('from_col'))
    to_row = int(data.get('to_row'))
    to_col = int(data.get('to_col'))

    board_data = game_logic.load_board(board_id)
    if board_data is None:
        return jsonify({'error': 'Game not found'}), 404

    # The move_piece function returns True/False and modifies board_data in place.
    old_spot = (from_row, from_col)
    new_spot = (to_row, to_col)
    success = game_logic.move_piece(board_data, old_spot, new_spot)

    if not success:
        return jsonify({'error': 'Illegal move'}), 400

    # After a successful move, board_data is already updated in memory and database.
    # We just return the new board state.
    return jsonify({
        'board_id': board_data['board_id'],
        'turn': 'white' if board_data['turn_id'] == board_data['white_player'] else 'black',
        'check_state': board_data['check_state'],
        'board': board_to_json(board_data['board'])
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
