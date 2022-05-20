from flask import render_template, request, redirect

from article import Article, db, app


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page" + name + '-' + str(id)


@app.route('/create_article', methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        db.session.add(article)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template("create_article.html")


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date).all()
    return render_template("posts.html", articles=articles)


@app.route('/posts/<int:id>')
def posts_detail(id):
    article = Article.query.get(id)
    return render_template("post_detail.html", article=article)


@app.route('/posts/<int:id>/del')
def posts_delete(id):
    article = Article.query.get_or_404(id)

    db.session.delete(article)
    db.session.commit()
    return redirect('/posts')


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):
    article = Article.query.get(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        db.session.commit()
        return redirect('/posts')
    else:
        return render_template("post_update.html", article=article)


if __name__ == "__main__":
    app.run(debug=True)
