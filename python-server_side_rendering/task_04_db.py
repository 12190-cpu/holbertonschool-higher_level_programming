#!/usr/bin/python3
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    with open('products.json') as f:
        return json.load(f)


def read_csv():
    data = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()

    conn.close()

    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })

    return data


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        elif source == 'sql':
            data = read_sql()
        else:
            return render_template('product_display.html', error="Wrong source")

        if product_id:
            data = [p for p in data if str(p.get('id')) == product_id]

            if not data:
                return render_template('product_display.html', error="Product not found")

        return render_template('product_display.html', products=data)

    except Exception:
        return render_template('product_display.html', error="Error loading data")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    