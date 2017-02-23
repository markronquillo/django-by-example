Building an e-Learning Platform
-------------------------------

Create fixtures for your models
Use model inheritance
Create custom model fields
Use class-based views and mixins
Build formsets
Manage groups and permissions
Create a content management system

A module contains multiple contents, so we define a ForeignKey field to the Module model. We also setup a generic relation to associate objects fomr different models that represetn different types of content

- content_type: A ForeignKey field to the ContentType model
- object_id: This is PositiveIntegerField to store the primary key of the related object
- item: A GenericForeignKey field to the related object by combining the two previous fields.


The Content model of our courses application contains a generic relation to associate different types of content ot it.



### Creating custom model fields

We need a field that allows us to specify an order for objects. We can create a custom field that inherits from PostiiveIntegerField and provides additional behavior.

There are two relevant functionalites that we will build into our order field:

- Automatically assign an order value when no specific order is provided. When no order is provided while storing an object, our field should automatically assign the next order based on the last existing ordered object. If there are two objects with order 1 and 2 respectively, when saving a thrid object, we should automatically assign thte order 3 to it fi no specific order is given
- Order objects with respect to other fields. Course modules will be ordered with respeect to the course they belong to and module contents with respect to the module they belong to.


### CMS

Login to the CMS
List the courses created by the instructo
Create, edit and delete courses
Add modules to a course and re-order them
Add different types of content to each module and re-order contents.


#### Creating class-based views


#### Using formsets

Django comes with an abstraction layer to work with multiplke forms on the same page. These groups of forms are known as formsets.

Formsets manage multiple instances of certain Form or ModelForm


The CourseModuleUpdateView handles the formset to add, update and delete modules for a specific course.

- TemplateResponseMixin: This mixin takes charge of rendering tmeplates and returning an HTTP response. It requires a template_name attribute that indicates the template to be rendered and provides the render_to_response() method to pass it a context and render the template.

- get_formset(): helper method that returns the formset

- dispatch(): this method is provided by the View class. it takes an HTTP request and its parameters and attempts to delegate to a lowercase method taht matches the HTTP method used.


#### Adding content to course modules

ContentCreateUpdateView

> if you are wondering if how does the app knows what kind of field to show in the form i.e. text, file upload etc., remember that it is defined in the models.py and the modelform_factory() creates a form given a model.




Caching Content
---------------------------

Create publis views for displaying course information
Build a student registration system
Manage student enrollment in courses
Render diverse course contents
Cache content using the cache framework


CourseListView

We retrieve all subjects, including the total number of courses for each of them. We use the ORM's annotate() method with the Count() aggregation function for doing so.



