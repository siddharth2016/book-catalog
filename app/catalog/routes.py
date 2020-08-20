from app.catalog import main


@main.route('/')
def sample():
    return "Hello World"
