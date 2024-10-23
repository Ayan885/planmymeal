from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Sample meal data with macro-nutrients (could be stored in a database or an external API)
with open("meals_data.json", "r") as f:
    MEALS_DATA = json.load(f)

def suggest_meals(proteins, carbs, fats, calories):
    suggested_meals = []

    for meal in MEALS_DATA:
        meal_proteins = meal['proteins']
        meal_carbs = meal['carbs']
        meal_fats = meal['fats']
        meal_calories = meal['calories']

        if (proteins <= meal_proteins and
            carbs <= meal_carbs and
            fats <= meal_fats and
            calories <= meal_calories):
            suggested_meals.append(meal)

    return suggested_meals

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest_meals', methods=['POST'])
def suggest():
    proteins = float(request.form['proteins'])
    carbs = float(request.form['carbs'])
    fats = float(request.form['fats'])
    calories = float(request.form['calories'])

    suggested_meals = suggest_meals(proteins, carbs, fats, calories)

    return jsonify(suggested_meals)

if __name__ == '__main__':
    app.run(debug=True)

