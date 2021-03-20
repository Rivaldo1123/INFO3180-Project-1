"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from .forms import PropertyForm
from .models import PropertyProfile
from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/property', methods= ['GET', 'POST'])
def property():
    propertyForm = PropertyForm()
    if request.method == "POST":
        if propertyForm.validate_on_submit():
            propertyPhoto = propertyForm.photo.data
            filename = secure_filename(propertyPhoto.filename)
            propertyPhoto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            title = propertyForm.title.data
            description = propertyForm.description.data
            bedrooms = propertyForm.bedrooms.data
            bathrooms = propertyForm.bathrooms.data
            location = propertyForm.location.data
            price = propertyForm.price.data
            proptype = propertyForm.proptype.data

            prop =  PropertyProfile(title,description,bedrooms,bathrooms,location,price,proptype,filename)
            
            db.session.add(prop)
            db.session.commit()
            
            flash('Property Added','success')
            return redirect(url_for('properties'))
        else:
            flash(flash_errors(propertyForm))
    return render_template('property.html', form = propertyForm)

@app.route('/properties')
def properties():
    props = PropertyProfile.query.all()
    return render_template('properties.html', props = props)


@app.route('/property/<int:propid>') 
def myproperty(propid = 1):

    props = PropertyProfile.query.filter_by(id = propid).first()

    return render_template('myproperty.html', prop = props)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
