from app import create_app

app = create_app()

if __name__ == '__main__':
    print('Starting flask dev server on port 5000...', flush=True)
    app.run(host='0.0.0.0')
