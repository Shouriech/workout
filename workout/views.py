from flask import Blueprint,render_template, request, redirect, flash,g, url_for
from werkzeug.exceptions import abort

from workout.auth import login_required
from workout.db import get_db

bp = Blueprint('workout', __name__)

@bp.route('/')
def index():
    db = get_db()
    workouts = db.execute(
        'SELECT w.id, workout_name, sets, reps, weight, date'
        ' FROM workout w JOIN user u ON w.user_id = u.id'
        ' ORDER BY date DESC'
    ).fetchall()
    return render_template('workout/index.html', workouts=workouts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        workout_name = request.form['workout_name']
        sets = request.form['sets']
        reps = request.form['reps']
        weight = request.form['weight']
        error = None

        if not workout_name:
            error = 'Workout name is required.'
        elif not sets:
            error = 'Sets are required.'
        elif not reps:
            error = 'Reps are required.'
        elif not weight:
            error = 'Weight is required.'
        
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db .execute(
                'INSERT INTO workout (workout_name, sets, reps, weight, user_id) VALUES (?, ?, ?, ?, ?)',
                (workout_name,sets,reps, g.user['id'])
            ) 
            db.commit()
            return redirect(url_for('workout.index'))

