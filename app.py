from flask import (render_template, redirect, 
                    url_for, request)
from models import db, Project, app
from datetime import datetime


@app.route('/')
# homepage
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


@app.route('/skills')
def skills():
    projects = Project.query.all()
    return render_template('skills.html', projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
# create route
def add_project():
    projects = Project.query.all()
    if request.form:
        date = datetime.strptime(request.form['date'], '%Y-%m')
        new_project = Project(title=request.form['title'], date=date, 
                        description=request.form['description'], skills=request.form['skills'], 
                        github=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=projects)


@app.route('/projects/<id>')
# detail route
def get_info(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project, projects=projects)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
# edit project
def edit_project(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    if request.form:
        project.title=request.form['title']
        project.date=request.form['date']
        project.description=request.form['description']
        project.skills=request.form['skills']
        project.github=request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', project=project, projects=projects)


@app.route('/projects/<id>/delete')
# delete project
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
# 404 error page
def not_found(error):
    return render_template('404.html', msg=error)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')