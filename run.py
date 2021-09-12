from personalWebsite import create_test_app

app = create_test_app()

if __name__  == '__main__':
    app.run(debug=True, host='0.0.0.0')
