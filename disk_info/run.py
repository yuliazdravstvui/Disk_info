from app import app

if __name__ == '__main__':
    print("\nЗапуск приложения 'Анализ хранилища'")
    print("Открыть в браузере: http://127.0.0.1:5000")
    print("Остановить: Ctrl+C\n")
    app.run(host='0.0.0.0', port=5000, debug=True)