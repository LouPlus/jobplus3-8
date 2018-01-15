from simplejob.app import create_app

app = create_app('development')

if __name__ == 'main':
    app.run()
