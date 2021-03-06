from flask import Flask
app = Flask(__name__)

@app.route('/user/')
def show_user_profile():
    # show the user profile for that user
    return 'Hello World!'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@app.errorhandler(404)
def page_not_found(e):
    return '404! Not Found, April Fool'