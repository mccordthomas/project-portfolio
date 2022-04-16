from flask import (render_template, redirect, 
                    url_for, request)
from models import db, Project, app


@app.route('/')
# homepage
def index():
    return render_template('index.html')


@app.route('/projects/new', methods=['GET', 'POST'])
# create route
def add_project():
    if request.form:
        new_project = Project(title=request.form['title'], date=request.form['date'], 
                        description=request.form['description'], skills=request.form['skills'], 
                        repo_link=request.form['repo_link'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', methods=['GET', 'POST'])


@app.route('/projects/<id>')
# detail route
def get_info(id):
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
# edit project
def edit_project(id):
    project = Project.query.get_or_404(id)
    if request.form:
        project.title=request.form['title']
        project.date=request.form['date']
        project.description=request.form['description']
        project.skills=request.form['skills']
        project.repo_link=request.form['repo_link']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', project=project)


@app.route('/about')
def about():
    pass


@app.route('/projects/<id>/delete')
# delete project
def delete_project():
    pass


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')