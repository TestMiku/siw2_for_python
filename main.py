import pandas as pd
import numpy as np
import webbrowser

data = pd.read_csv('programming language trend over time.csv')
data['Week'] = pd.to_datetime(data['Week'])

print("Введите диапазон дат, для которого вы хотите получить результаты:")

oldest_date = data['Week'].min().strftime('%Y-%m-%d')
newest_date = data['Week'].max().strftime('%Y-%m-%d')
print(f"Самая старая дата в наборе данных: {oldest_date}")
print(f"Самая новая дата в наборе данных: {newest_date}")

while True:
    try:
        start_date_input = input("Введите дату начала диапазона (ГГГГ-ММ-ДД): ")
        start_date = pd.to_datetime(start_date_input)
        
        if start_date < data['Week'].min() or start_date > data['Week'].max():
            print("Ошибка: Введенная дата находится вне диапазона дат набора данных.")
        else:
            break
    except pd._libs.tslibs.parsing.DateParseError:
        print("Ошибка: Неверный формат даты. Попробуйте снова.")

while True:
    try:
        end_date_input = input("Введите дату окончания диапазона (ГГГГ-ММ-ДД): ")
        end_date = pd.to_datetime(end_date_input)
        
        if end_date < data['Week'].min() or end_date > data['Week'].max():
            print("Ошибка: Введенная дата находится вне диапазона дат набора данных.")
        elif end_date < start_date:
            print("Ошибка: Дата окончания диапазона должна быть после даты начала.")
        else:
            break
    except pd._libs.tslibs.parsing.DateParseError:
        print("Ошибка: Неверный формат даты. Попробуйте снова.")

filtered_data = data[(data['Week'] >= start_date) & (data['Week'] <= end_date)]

# Расчет среднего значения с использованием NumPy
averages = filtered_data.mean()
python_average = np.mean(filtered_data['Python'])
java_average = np.mean(filtered_data['Java'])
c_plus_average = np.mean(filtered_data['C++'])

# Расчет максимального значения с использованием NumPy
maximums = filtered_data.max()
python_max = np.max(filtered_data['Python'])
java_max = np.max(filtered_data['Java'])
c_plus_max = np.max(filtered_data['C++'])

# Расчет минимального значения с использованием NumPy
minimums = filtered_data.min()
python_min = np.min(filtered_data['Python'])
java_min = np.min(filtered_data['Java'])
c_plus_min = np.min(filtered_data['C++'])

print("\nРезультаты:")
print("Средние значения:")
print(f"Python: {python_average}")
print(f"Java: {java_average}")
print(f"C++: {c_plus_average}")
print("\nМаксимальные значения:")
print(f"Python: {python_max}")
print(f"Java: {java_max}")
print(f"C++: {c_plus_max}")
print("\nМинимальные значения:")
print(f"Python: {python_min}")
print(f"Java: {java_min}")
print(f"C++: {c_plus_min}")

html_content = f"""
<html>
<head>
  <title>Анализ трендов языков программирования</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 50px;
    }}
    h1 {{
      color: #333;
    }}
    table {{
      border-collapse: collapse;
      width: 50%;
    }}
    th, td {{
      padding: 8px;
      text-align: left;
      border-bottom: 1px solid #ddd;
    }}
    th {{
      background-color: #f2f2f2;
    }}
  </style>
</head>
<body>
  <h1>Анализ трендов языков программирования</h1>
  <table>
    <tr>
      <th>Язык</th>
      <th>Средний балл</th>
      <th>Максимальный балл</th>
      <th>Минимальный балл</th>
    </tr>
    <tr>
      <td>Python</td>
      <td>{python_average}</td>
      <td>{python_max}</td>
      <td>{python_min}</td>
    </tr>
    <tr>
      <td>Java</td>
      <td>{java_average}</td>
      <td>{java_max}</td>
      <td>{java_min}</td>
    </tr>
    <tr>
      <td>C++</td>
      <td>{c_plus_average}</td>
      <td>{c_plus_max}</td>
      <td>{c_plus_min}</td>
    </tr>
  </table>
</body>
</html>
"""

with open('analysis_results.html', 'w') as f:
    f.write(html_content)

webbrowser.open('analysis_results.html')
