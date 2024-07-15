
      <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <p>Server-side rendering is a powerful technique where web pages are generated on the server and sent to the client as fully formed HTML. This contrasts with client-side rendering, where the browser builds the web page using JavaScript and dynamic data. Through this project, you will learn how to implement SSR using Python and Flask, leveraging the Jinja templating engine to create dynamic, efficient, and SEO-friendly web applications.</p>

<h3>Learning Objectives</h3>

<ul>
<li>Understand the concepts of server-side rendering and how it differs from client-side rendering.</li>
<li>Learn the benefits of using server-side rendering in web development.</li>
<li>Implement SSR in Python using the Flask framework.</li>
<li>Utilize Jinja templating engine to dynamically generate HTML pages.</li>
<li>Read and display data from various sources including JSON, CSV, and SQLite databases.</li>
<li>Handle dynamic content and user inputs in web applications.</li>
</ul>

<h3>What to Expect</h3>

<p>In this project, you will build a Flask application that serves web pages using server-side rendering techniques. You will start by creating basic templates and gradually move towards integrating dynamic content from multiple data sources. By the end of the project, you will have a comprehensive understanding of SSR, templating, and how to build efficient, scalable web applications.</p>

<h3>Resources</h3>

<ul>
<li><strong>MDN Web Docs on Server-Side Web Development:</strong> <a href="/rltoken/vEsedYcUIdF67j4xmQqrAw" title="MDN Server-Side Web Development" target="_blank">MDN Server-Side Web Development</a></li>
<li><strong>Client-side vs. Server-side vs. Pre-rendering for Web Apps:</strong> <a href="/rltoken/FErUnxmyagdWQmd1od8Yhg" title="Templating Engines in Web Development" target="_blank">Templating Engines in Web Development</a></li>
<li><strong>Flask Documentation:</strong> <a href="/rltoken/NIjNxWgVHtpYDjsR0mUFzA" title="Flask Official Documentation" target="_blank">Flask Official Documentation</a></li>
<li><strong>Python JSON Documentation:</strong> <a href="/rltoken/lC6m9GFhAWqgqvmSlA3y5g" title="Python JSON Documentation" target="_blank">Python JSON Documentation</a></li>
<li><strong>Python CSV Documentation:</strong> <a href="/rltoken/FwAYKq-BrdtZlNodGDxsag" title="Python CSV Documentation" target="_blank">Python CSV Documentation</a></li>
<li><strong>Python SQLite Documentation:</strong> <a href="/rltoken/wPc6yZmq5N00DfY5cfWRYQ" title="Python SQLite Documentation" target="_blank">Python SQLite Documentation</a></li>
<li><strong>Jinja2 Documentation:</strong> <a href="/rltoken/Hz3FkY15qDQWE31oBwe-eA" title="Jinja2 Documentation" target="_blank">Jinja2 Documentation</a></li>
</ul>

<p>This project will equip you with the skills needed to implement server-side rendering in your web applications, making them more efficient, SEO-friendly, and easy to maintain.</p>

  </div>
</div>







          <h2 class="gap">Tasks</h2>

    <div data-role="task30419" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-30419">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Creating a Simple Templating Program
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="8687"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>In this task, you will create a Python function that generates personalized invitation files from a template with placeholders and a list of objects. Each output file should be named sequentially, starting from 1. You will also implement specific error handling for various edge cases.</p>

<h3>Objective</h3>

<ul>
<li>Understand how to use string templating in Python.</li>
<li>Implement file operations for reading templates and writing output files.</li>
<li>Handle various edge cases and errors gracefully.</li>
</ul>

<hr>

<h3>Instructions</h3>

<ol>
<li><p><strong>Create the Template:</strong></p>

<ul>
<li>Use the provided template with placeholders for <code>name</code>, <code>event_title</code>, <code>event_date</code>, and <code>event_location</code>.</li>
</ul></li>
<li><p><strong>Define the Data:</strong></p>

<ul>
<li>Use the provided list of objects as your data source.</li>
</ul></li>
<li><p><strong>Write the Templating Function:</strong></p>

<ul>
<li>Define a function named <code>generate_invitations</code> that takes two parameters: <code>template</code> and <code>attendees</code>.</li>
</ul></li>
</ol>

<ul>
<li><p><strong>Check Input Types:</strong></p>

<ul>
<li>Verify that <code>template</code> is a string and <code>attendees</code> is a list of dictionaries.</li>
<li>If <code>template</code> is not a string or <code>attendees</code> is not a list of dictionaries, log an error message and terminate the function.</li>
</ul></li>
<li><p><strong>Handle Empty Inputs:</strong></p>

<ul>
<li>Check if the template is empty and log an error message if it is.</li>
<li>Check if the attendees list is empty and log an error message if it is.</li>
</ul></li>
<li><p><strong>Process Each Attendee:</strong></p>

<ul>
<li>Iterate over the list of attendees and replace the placeholders in the template with the corresponding values from each attendee’s dictionary.</li>
<li>If a value is missing, replace it with “N/A”.</li>
</ul></li>
<li><p><strong>Generate Output Files:</strong></p>

<ul>
<li>Write the processed template to output files named <code>output_X.txt</code>, where <code>X</code> is the index of the attendee starting from 1.</li>
</ul></li>
</ul>

<ol>
<li><strong>Specific Error Handling Behaviors:</strong>

<ul>
<li><strong>Empty Template:</strong> If the template is empty, log an error message, “Template is empty, no output files generated.” and terminate without creating any files.</li>
<li><strong>Empty List of Objects:</strong> If the list of objects is empty, log a message, “No data provided, no output files generated.” and terminate without creating any files.</li>
<li><strong>Missing Data in Object:</strong> If an object is missing data for any of the placeholders, replace the missing data with the text “N/A” in the output file. For example, if <code>event_date</code> is missing, it should appear as “event_date: N/A” in the output.</li>
<li><strong>Invalid Input Types:</strong> If the input template is not a string or the list is not a list of dictionaries, log an error message indicating the type of invalid input and terminate the function.</li>
</ul></li>
</ol>

<hr>

<h3>Template File: <code>template.txt</code></h3>

<pre><code class="text">Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
</code></pre>

<h3>Example Data for Testing:</h3>

<pre><code class="python">attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]
</code></pre>

<h3>Example Main File to Test the Program:</h3>

<pre><code class="python"># Main file content
from task_00_intro import generate_invitations

# Read the template from a file
with open('template.txt', 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)
</code></pre>

<hr>

<h3>Hints:</h3>

<ul>
<li>Use Python’s string <code>replace</code> method to substitute placeholders with actual values.</li>
<li>Use <code>os.path.exists</code> to check if a file already exists before writing.</li>
<li>Use <code>try</code> and <code>except</code> blocks to handle potential errors gracefully.</li>
</ul>

<hr>

<h3>Resources:</h3>

<ul>
<li><strong>Python String Methods</strong>: <a href="/rltoken/W6bJdwDnBI2Ei0brfUqCJw" title="Python Official Documentation" target="_blank">Python Official Documentation</a></li>
<li><strong>File Handling in Python</strong>: <a href="/rltoken/1T4vhH1weF8SheeeZYeeLA" title="Python Official Documentation" target="_blank">Python Official Documentation</a></li>
</ul>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-server_side_rendering</code></li>
            <li>File: <code>task_00_intro.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="30419" data-batch-id="558" data-toggle="modal" data-target="#task-30419-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-30419-users-done-modal" data-task-id="30419" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "0. Creating a Simple Templating Program"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-30419-score-info-score">0</span>/10
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task30420" data-position="2" id="task-num-1">
      <div class="panel panel-default task-card " id="task-30420">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Creating a Basic HTML Template in Flask
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="8687"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>In this task, you will build a basic Flask application that serves a web page using a Jinja template. You will create a simple HTML template that includes various elements like headings, paragraphs, and lists, and learn how to render it as a web page using Flask. Additionally, you will learn to create reusable templates for headers and footers to promote code reusability and consistency across multiple pages.</p>

<h3>Objective</h3>

<ul>
<li>Set up a Flask environment and create a basic Flask application.</li>
<li>Design HTML templates using Jinja for dynamic content rendering.</li>
<li>Implement reusable components in templates to maintain consistent layout across pages.</li>
</ul>

<hr>

<h3>Instructions</h3>

<ol>
<li><p><strong>Set Up Your Flask Environment:</strong></p>

<ul>
<li>Ensure Python is installed on your system.</li>
<li>Install Flask using pip:
<code>sh
pip install Flask
</code></li>
</ul></li>
<li><p><strong>Create a Basic Flask Application:</strong></p>

<ul>
<li>In your project directory, create a Python file named <code>task_01_jinja.py</code>.</li>
<li>Write a basic Flask application with a route that renders an HTML template.</li>
</ul></li>
</ol>

<p>Example:</p>

<pre><code class="python">   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/')
   def home():
       return render_template('index.html')

   if __name__ == '__main__':
       app.run(debug=True, port=5000)
</code></pre>

<ol>
<li><strong>Design Your HTML Template:</strong>

<ul>
<li>In a <code>templates</code> folder within your project directory, create an HTML file named <code>index.html</code>.</li>
<li>Design a simple HTML page with a heading (<code>&lt;h1&gt;</code>), a paragraph (<code>&lt;p&gt;</code>), and an unordered list (<code>&lt;ul&gt;</code> with <code>&lt;li&gt;</code> items).</li>
</ul></li>
</ol>

<p>Example content for <code>index.html</code>:</p>

<pre><code class="html">   &lt;!doctype html&gt;
   &lt;html lang="en"&gt;
   &lt;head&gt;
       &lt;title&gt;My Flask App&lt;/title&gt;
   &lt;/head&gt;
   &lt;body&gt;
       &lt;h1&gt;Welcome to My Flask App&lt;/h1&gt;
       &lt;p&gt;This is a simple Flask application.&lt;/p&gt;
       &lt;ul&gt;
           &lt;li&gt;Flask&lt;/li&gt;
           &lt;li&gt;HTML&lt;/li&gt;
           &lt;li&gt;Templates&lt;/li&gt;
       &lt;/ul&gt;
   &lt;/body&gt;
   &lt;/html&gt;
</code></pre>

<ol>
<li><p><strong>Render the Template in Flask:</strong></p>

<ul>
<li>Use Flask’s <code>render_template</code> function to render the HTML template when the corresponding route is accessed.</li>
</ul></li>
<li><p><strong>Create Reusable Header and Footer Templates:</strong></p>

<ul>
<li>In the <code>templates</code> folder, create two new HTML files: <code>header.html</code> and <code>footer.html</code>.</li>
<li>Design simple but distinct layouts for the header and footer, and include navigation links (Home, About, Contact) to all pages into header file.
Example content for <code>header.html</code>:</li>
</ul></li>
</ol>

<pre><code class="html">   &lt;header&gt;
       &lt;h1&gt;My Flask App&lt;/h1&gt;
   &lt;/header&gt;
</code></pre>

<p>Example content for <code>footer.html</code>:
   <code>html
   &lt;footer&gt;
       &lt;p&gt;&amp;copy; 2024 My Flask App&lt;/p&gt;
   &lt;/footer&gt;
</code></p>

<ol>
<li><p><strong>Design Multiple Pages with Shared Header and Footer:</strong></p>

<ul>
<li>Create additional HTML pages for different content such as <code>about.html</code> and <code>contact.html</code>.</li>
<li>In each of these pages (<code>index.html</code>, <code>about.html</code> and <code>contact.html</code>), include the header and footer templates without duplicating their code.</li>
<li>Add specific tags for each page:
-In about.html, include an   <code>&lt;h1&gt;</code> tag with the text “About Us” and a paragraph (<code>&lt;p&gt;</code>) with content describing the page.
-In contact.html, include an  <code>&lt;h1&gt;</code>  tag with the text “Contact Us” and a paragraph ((<code>&lt;p&gt;</code>) with content for the contact page.</li>
</ul></li>
<li><p><strong>Modify Flask Routes:</strong></p>

<ul>
<li>Add new routes in your Flask application corresponding to the additional pages you created.</li>
</ul></li>
</ol>

<p>Example:</p>

<pre><code class="python">   @app.route('/about')
   def about():
       return render_template('about.html')

   @app.route('/contact')
   def contact():
       return render_template('contact.html')
</code></pre>

<hr>

<h3>Hints:</h3>

<ul>
<li>Ensure your Flask application runs on port 5000.</li>
<li>Use the <code>render_template</code> function from Flask to render HTML templates.</li>
<li>Utilize Jinja’s <code>{% include %}</code> statement to include reusable components like headers and footers.</li>
</ul>

<hr>

<h3>Resources:</h3>

<ul>
<li><strong>Flask Quickstart:</strong> <a href="/rltoken/xLnef6coA0Lgt71gTcnS5Q" title="Flask Quickstart" target="_blank">Flask Quickstart</a></li>
<li><strong>HTML Basics:</strong> <a href="/rltoken/3s9aM9mrDsmWx6I-V7zokw" title="HTML Tutorial on W3Schools" target="_blank">HTML Tutorial on W3Schools</a></li>
<li><strong>Flask Templating with Jinja:</strong> <a href="/rltoken/RWlt7-FqgostaP1MpAJnXg" title="Flask Templating" target="_blank">Flask Templating</a></li>
<li><strong>Jinja Template Inheritance:</strong> <a href="/rltoken/oT7L0anPHrZ-Q42K1Lp8ig" title="Jinja Template Inheritance" target="_blank">Jinja Template Inheritance</a></li>
</ul>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-server_side_rendering</code></li>
            <li>File: <code>task_01_jinja.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="30420" data-batch-id="558" data-toggle="modal" data-target="#task-30420-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-30420-users-done-modal" data-task-id="30420" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "1. Creating a Basic HTML Template in Flask"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-30420-score-info-score">0</span>/4
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task30421" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-30421">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Creating a Dynamic Template with Loops and Conditions in Flask
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="8687"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>In this task, you will enhance your Flask application by integrating dynamic content into your HTML templates using Jinja’s loop and conditional constructs. You will read a list of items from a JSON file and display them dynamically on a web page.</p>

<h3>Objective</h3>

<ul>
<li>Use Jinja’s loop and conditional constructs to dynamically render content in HTML templates.</li>
<li>Read and parse JSON data in Python.</li>
<li>Integrate dynamic content into your Flask application.</li>
</ul>

<hr>

<h3>Instructions</h3>

<ol>
<li><p><strong>Prepare Your Flask Application:</strong></p>

<ul>
<li>Continue using the Flask application you created in the previous exercises.</li>
<li>Ensure you have a basic understanding of Jinja’s templating syntax.</li>
</ul></li>
<li><p><strong>Create a Dynamic Template:</strong></p>

<ul>
<li>In your <code>templates</code> folder, create a new HTML template named <code>items.html</code> with “Items List” for the title.</li>
<li>This template should include a loop to iterate over a list of items and display each item.</li>
<li>Items must be displayed as an <strong>unordered list</strong>.</li>
<li>Add a conditional statement to display a message “<strong>No items found</strong>” if the list is empty.</li>
</ul></li>
<li><p><strong>Define the Data for the Template:</strong></p>

<ul>
<li>In your project directory, create a file named <code>items.json</code>.</li>
<li>Populate <code>items.json</code> with a list of items. Example:
<code>json
{
 "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
}
</code></li>
<li>Experiment with different lists, including an empty list, to see how your template responds.</li>
</ul></li>
<li><p><strong>Add a Route in Flask:</strong></p>

<ul>
<li>Create a new route <code>/items</code> in your Flask application to render the <code>items.html</code> template with the list of items.</li>
<li>Use Python’s <code>json</code> module to read the data from <code>items.json</code>.</li>
<li>Pass the list of items to the template for rendering.</li>
</ul></li>
</ol>

<hr>

<h3>Example Data for Testing:</h3>

<pre><code class="json">{
    "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
}
</code></pre>

<hr>

<h3>Hints:</h3>

<ul>
<li>Use Python’s <code>json</code> module to read data from the JSON file.</li>
<li>Utilize Jinja’s <code>{% for %}</code> loop to iterate over the list of items in the template.</li>
<li>Use the <code>{% if %}</code> statement to conditionally display the message when the list is empty.</li>
<li>Define the new route <code>/items</code> in your Flask application and use the <code>render_template</code> function to pass the list of items to <code>items.html</code>.</li>
</ul>

<hr>

<h3>Resources:</h3>

<ul>
<li><strong>Jinja Template Designer Documentation:</strong> <a href="/rltoken/8JdOhBd-JaExBWwtyVJuew" title="Jinja Template Designer Documentation" target="_blank">Jinja Template Designer Documentation</a></li>
<li><strong>Flask Templating with Jinja:</strong> <a href="/rltoken/RWlt7-FqgostaP1MpAJnXg" title="Flask Templating" target="_blank">Flask Templating</a></li>
</ul>

<hr>

<h3>Testing Your Application:</h3>

<p>After setting up the dynamic template and route, run your Flask application and navigate to the new route. Verify that the list of items is correctly displayed on the page. Test with different lists, including an empty list, to ensure that the conditional statement works as expected.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-server_side_rendering</code></li>
            <li>File: <code>task_02_logic.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="30421" data-batch-id="558" data-toggle="modal" data-target="#task-30421-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-30421-users-done-modal" data-task-id="30421" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "2. Creating a Dynamic Template with Loops and Conditions in Flask"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-30421-score-info-score">0</span>/2
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task30422" data-position="4" id="task-num-3">
      <div class="panel panel-default task-card " id="task-30422">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Displaying Data from JSON or CSV Files in Flask
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="8687"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>In this task, you will build a feature in your Flask application to read and display product data from two different data formats: JSON and CSV. You will create a single HTML template that can display data from either file type, depending on a query parameter provided in the URL. You will add functionality to your Flask application to filter product data based on an optional <code>id</code> query parameter. Additionally, you will handle edge cases such as invalid <code>source</code> parameter values or when the specified <code>id</code> is not found in the data.</p>

<h3>Objective</h3>

<ul>
<li>Read and parse data from JSON and CSV files.</li>
<li>Use query parameters in Flask to determine data sources and filter criteria.</li>
<li>Implement error handling for invalid inputs and missing data.</li>
<li>Render dynamic data in HTML templates using Jinja.</li>
</ul>

<hr>

<h3>Instructions</h3>

<ol>
<li><p><strong>Prepare Data Files:</strong></p>

<ul>
<li>Create a JSON file (<code>products.json</code>) containing a list of products, each with an <code>id</code>, <code>name</code>, <code>category</code>, and <code>price</code>.
Example JSON content:
<code>json
[
{"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
{"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]
</code></li>
<li>Create a CSV file (<code>products.csv</code>) with similar data, using columns for <code>id</code>, <code>name</code>, <code>category</code>, and <code>price</code>.
Example CSV content:
<code>
id,name,category,price
1,Laptop,Electronics,799.99
2,Coffee Mug,Home Goods,15.99
</code></li>
</ul></li>
<li><p><strong>Create a Dynamic Template:</strong></p>

<ul>
<li>In your <code>templates</code> folder, create an HTML template <code>product_display.html</code> for displaying the product data.</li>
<li>Design the template to display the data in a table format with headings for Name, Category, and Price.</li>
</ul></li>
<li><p><strong>Modify Flask Application:</strong></p>

<ul>
<li>In <code>task_03_files.py</code>, create a route in your Flask application that accepts a <code>source</code> query parameter (values <code>json</code> or <code>csv</code>) and an optional <code>id</code>.</li>
<li>Depending on the <code>source</code> parameter, read and parse data from the corresponding file.</li>
<li>Implement logic to filter data by the specified <code>id</code> if provided. If <code>id</code> is not provided, display all products.</li>
<li>Pass the parsed data to the <code>product_display.html</code> template for rendering.</li>
</ul></li>
<li><p><strong>Implement File Reading Logic:</strong></p>

<ul>
<li>Write functions to read and parse data from both JSON and CSV files.</li>
<li>Ensure the data is converted into a format that can be easily displayed by the template.</li>
</ul></li>
<li><p><strong>Handle Edge Cases:</strong></p>

<ul>
<li>If <code>source</code> is neither <code>json</code> nor <code>csv</code>, return a “Wrong source” error message in the template.</li>
<li>If <code>id</code> is provided but not found in the file, display a “Product not found” error message in the template.</li>
<li>Modify the <code>product_display.html</code> template to handle and display error messages if necessary.</li>
</ul></li>
</ol>

<hr>

<h3>Hints:</h3>

<ul>
<li>Use Python’s <code>json</code> module to read data from the JSON file.</li>
<li>Use Python’s <code>csv</code> module to read data from the CSV file.</li>
<li>Utilize Flask’s <code>request.args</code> to get query parameters.</li>
<li>Use Jinja’s templating features to conditionally display error messages and dynamic data.</li>
</ul>

<hr>

<h3>Resources:</h3>

<ul>
<li><strong>Reading JSON and CSV in Python:</strong>

<ul>
<li>JSON: <a href="/rltoken/lC6m9GFhAWqgqvmSlA3y5g" title="JSON in Python" target="_blank">JSON in Python</a></li>
<li>CSV: <a href="/rltoken/FwAYKq-BrdtZlNodGDxsag" title="CSV File Reading and Writing" target="_blank">CSV File Reading and Writing</a></li>
</ul></li>
<li><strong>Flask Request Object:</strong> <a href="/rltoken/eQhOfyVFkLC5gR3NhPoVsA" title="Flask Request Object" target="_blank">Flask Request Object</a></li>
<li><strong>Query Parameters in Flask:</strong> <a href="/rltoken/eQhOfyVFkLC5gR3NhPoVsA" title="Flask Request Object" target="_blank">Flask Request Object</a></li>
<li><strong>Error Handling in Flask:</strong> <a href="/rltoken/c3p6vS48JY-Dvimfj3NPbw" title="Flask Error Handling" target="_blank">Flask Error Handling</a></li>
</ul>

<hr>

<h3>Testing Your Application:</h3>

<p>Test your application with various scenarios:</p>

<ul>
<li>Access URLs like <code>http://localhost:5000/products?source=json</code>, <code>http://localhost:5000/products?source=csv</code>, and <code>http://localhost:5000/products?source=xml</code> (invalid source).</li>
<li>Test with and without the <code>id</code> parameter, and with both valid and invalid <code>id</code> values.</li>
<li>Verify that the application correctly filters data, displays all products when no <code>id</code> is provided, and shows appropriate error messages for edge cases.</li>
</ul>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-server_side_rendering</code></li>
            <li>File: <code>task_03_files.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="30422" data-batch-id="558" data-toggle="modal" data-target="#task-30422-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-30422-users-done-modal" data-task-id="30422" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "3. Displaying Data from JSON or CSV Files in Flask"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-30422-score-info-score">0</span>/5
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task30423" data-position="5" id="task-num-4">
      <div class="panel panel-default task-card " id="task-30423">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. Extending Dynamic Data Display to Include SQLite in Flask
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="8687"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Building on the previous exercise, you will now add the functionality to fetch and display data from a SQLite database in your Flask application. The application should allow users to choose between JSON, CSV, and SQL (SQLite database) as data sources using the <code>source</code> query parameter.</p>

<h3>Objective</h3>

<ul>
<li>Set up and interact with a SQLite database in a Flask application.</li>
<li>Extend existing functionality to handle multiple data sources.</li>
<li>Implement error handling for database-related issues.</li>
</ul>

<hr>

<h3>Instructions</h3>

<ol>
<li><strong>Database Setup:</strong>

<ul>
<li><strong>SQLite Database File:</strong>

<ul>
<li>Name your SQLite database file <code>products.db</code>.</li>
</ul></li>
</ul></li>
</ol>

<ul>
<li><p><strong>Table Structure:</strong></p>

<ul>
<li>Create a <code>Products</code> table with columns: <code>id</code> (primary key), <code>name</code>, <code>price</code>, <code>category</code>.</li>
</ul></li>
<li><p><strong>Example Data:</strong></p>

<ul>
<li>Insert the following data into the <code>Products</code> table:

<ul>
<li><code>id</code>: 1, <code>name</code>: “Laptop”, <code>price</code>: 799.99, <code>category</code>: “Electronics”</li>
<li><code>id</code>: 2, <code>name</code>: “Coffee Mug”, <code>price</code>: 15.99, <code>category</code>: “Home Goods”</li>
</ul></li>
</ul></li>
</ul>

<p>Use the following script to create and populate the database:</p>

<pre><code class="python">   import sqlite3

   def create_database():
       conn = sqlite3.connect('products.db')
       cursor = conn.cursor()
       cursor.execute('''
           CREATE TABLE IF NOT EXISTS Products (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               category TEXT NOT NULL,
               price REAL NOT NULL
           )
       ''')
       cursor.execute('''
           INSERT INTO Products (id, name, category, price)
           VALUES
           (1, 'Laptop', 'Electronics', 799.99),
           (2, 'Coffee Mug', 'Home Goods', 15.99)
       ''')
       conn.commit()
       conn.close()

   if __name__ == '__main__':
       create_database()
</code></pre>

<ol>
<li><p><strong>Modify the Existing Dynamic Template:</strong></p>

<ul>
<li>Use the same HTML template (<code>product_display.html</code>) created in Task 3 for displaying product data.</li>
</ul></li>
<li><p><strong>Implement SQLite Data Source:</strong></p>

<ul>
<li>Extend the existing Flask route to handle <code>source=sql</code> as a query parameter.</li>
<li>Implement logic to fetch data from the SQLite database when this parameter is used.</li>
<li>Ensure that the same template is used to display data regardless of the source.</li>
</ul></li>
<li><p><strong>Handle Error Cases:</strong></p>

<ul>
<li>As in Task 3, display a “Wrong source” error message if an invalid <code>source</code> is provided.</li>
<li>Implement appropriate error handling for database-related errors.</li>
</ul></li>
</ol>

<hr>

<h3>Hints:</h3>

<ul>
<li>Use Python’s <code>sqlite3</code> module to interact with the SQLite database.</li>
<li>Define a function to read data from the SQLite database and convert it into a format suitable for rendering in the template.</li>
<li>Use Flask’s <code>request.args</code> to get the <code>source</code> query parameter and determine the data source.</li>
</ul>

<hr>

<h3>Resources:</h3>

<ul>
<li><strong>Flask-SQLAlchemy:</strong> <a href="/rltoken/JBmvcrjCCGZGlWw1M-OI3A" title="Flask-SQLAlchemy" target="_blank">Flask-SQLAlchemy</a></li>
<li><strong>SQLite in Python:</strong> <a href="/rltoken/wPc6yZmq5N00DfY5cfWRYQ" title="SQLite3 Module" target="_blank">SQLite3 Module</a></li>
</ul>

<hr>

<h3>Testing Your Application:</h3>

<p>Test your application with the URL query parameter set to <code>json</code>, <code>csv</code>, and <code>sql</code> to ensure that the correct data is displayed for each source. Verify that the application can handle and display errors appropriately for invalid sources or database issues.</p>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>python-server_side_rendering</code></li>
            <li>File: <code>task_04_db.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="30423" data-batch-id="558" data-toggle="modal" data-target="#task-30423-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-30423-users-done-modal" data-task-id="30423" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "4. Extending Dynamic Data Display to Include SQLite in Flask"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-30423-score-info-score">0</span>/9
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>



          <div class="gap">
  <div data-react-class="projects/ProjectReview" data-react-props="{&quot;correction&quot;:{&quot;statusURI&quot;:&quot;/corrections/877823/status_self_paced.json&quot;,&quot;startReviewURI&quot;:&quot;/corrections/877823/start_auto_review_self_paced.json&quot;},&quot;csrfToken&quot;:&quot;pq_b551q-nGFV_hbEHHufA8YXhGBD8rGPrgDZz4p34SuM6vrxTVqwJFiiwSvI-e7iwKABgS0FcyLeENDYpS3HQ&quot;,&quot;nextProject&quot;:{&quot;details&quot;:{&quot;curriculum_completed&quot;:false,&quot;message&quot;:&quot;Next project: ES6 Basics&quot;,&quot;uri&quot;:&quot;/projects/2345&quot;},&quot;fetchURI&quot;:&quot;/projects/3143/next&quot;},&quot;pollingInterval&quot;:10000,&quot;progress&quot;:{&quot;auto_review&quot;:{&quot;can_execute&quot;:true,&quot;completion&quot;:null,&quot;inability_to_execute_reason&quot;:null},&quot;tasks&quot;:[{&quot;id&quot;:30419,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:10,&quot;score&quot;:0}},{&quot;id&quot;:30420,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:4,&quot;score&quot;:0}},{&quot;id&quot;:30421,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:2,&quot;score&quot;:0}},{&quot;id&quot;:30422,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:5,&quot;score&quot;:0}},{&quot;id&quot;:30423,&quot;progress_score&quot;:{&quot;progress&quot;:0.0,&quot;score&quot;:0.0},&quot;score_info&quot;:{&quot;passed&quot;:false,&quot;points&quot;:9,&quot;score&quot;:0}}],&quot;summary&quot;:{&quot;completion&quot;:0.0,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null}},&quot;can_skip&quot;:true,&quot;can_start_peer_review&quot;:false},&quot;peerReview&quot;:{&quot;availableReviewersURI&quot;:&quot;/corrections/877823/available_reviewers.json&quot;,&quot;canReviewPeerDirectly&quot;:true,&quot;correctCorrectionURI&quot;:&quot;https://intranet.hbtn.io/corrections/877823/correct&quot;,&quot;qaReviewsURI&quot;:&quot;/corrections/to_review&quot;,&quot;readyForReviewURI&quot;:&quot;/corrections/877823/toggle_ready_for_review.json&quot;,&quot;reviewDeadline&quot;:null,&quot;synchronousManualReview&quot;:false},&quot;project&quot;:{&quot;completion&quot;:0.0,&quot;id&quot;:3143,&quot;index&quot;:0,&quot;isAccessible&quot;:true,&quot;isOptional&quot;:false,&quot;imagePath&quot;:&quot;/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png&quot;,&quot;name&quot;:&quot;Python - Server-Side Rendering&quot;,&quot;score&quot;:{&quot;mandatory&quot;:null,&quot;optional&quot;:null},&quot;tasksCount&quot;:0},&quot;skipURI&quot;:&quot;/corrections/877823/skip&quot;,&quot;taskLevelReviewTypeHumanized&quot;:&quot;Your score will be updated as you progress.&quot;}" data-react-cache-id="projects/ProjectReview-0"><div class="panel panel-default"><div class="panel-heading"><h3 class="panel-title">Score</h3></div><div class="panel-body"><div class="align-items-center d-flex gap-5"><div class="pathway" style="padding: 10px 30px 40px;"><div class="project-circle " style="border-radius: 100%; box-shadow: rgb(229, 230, 230) 10px 20px 10px; height: 125px; margin: auto; padding: 5px; width: 125px;"><div data-test-id="CircularProgressbarWithChildren"><div style="position: relative; width: 100%; height: 100%;"><svg class="CircularProgressbar " viewBox="0 0 100 100" data-test-id="CircularProgressbar" style="height: 115px; vertical-align: middle; width: 115px;"><path class="CircularProgressbar-trail" d="
      M 50,50
      m 0,-48.5
      a 48.5,48.5 0 1 1 0,97
      a 48.5,48.5 0 1 1 0,-97
    " stroke-width="3" fill-opacity="0" style="stroke-dasharray: 304.734px, 304.734px; stroke-dashoffset: 0px;"></path><path class="CircularProgressbar-path" d="
      M 50,50
      m 0,-48.5
      a 48.5,48.5 0 1 1 0,97
      a 48.5,48.5 0 1 1 0,-97
    " stroke-width="3" fill-opacity="0" style="stroke-dasharray: 304.734px, 304.734px; stroke-dashoffset: 304.734px;"></path></svg><div data-test-id="CircularProgressbarWithChildren__children" style="position: absolute; width: 100%; height: 100%; margin-top: -100%; display: flex; flex-direction: column; justify-content: center; align-items: center;"><div class="position-relative"><span data-container="body" data-html="false" data-placement="auto top" data-toggle="tooltip" title="" data-original-title="Python - Server-Side Rendering"><div class="align-items-center d-flex justify-content-center project-circle-body active" style="border-radius: 100%; height: 100px; width: 100px;"><img alt="Project badge" src="/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png" width="60%"></div></span></div></div></div></div></div></div><div style="flex-basis: 100%;"><p class="mb-2 text-primary"><span>Your score will be updated as you progress.</span></p><p>Please review <strong>all the tasks</strong> before you start the peer review.</p><div class="d-flex flex-wrap gap-3 justify-content-between mt-4"><div class="btn-group"><button class="btn btn-primary" id="project-launch-review-btn"><i aria-hidden="true" class="fa fa-paper-plane"></i><span class="ml-2">Review all the tasks</span></button></div><div></div></div></div></div></div></div></div>
</div>



          <div class="modal fade" id="sandboxes-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button><h4 class="modal-title">Recommended Sandboxes</h4></div><div class="modal-body"><div data-react-class="user_sandboxes/Sandboxes" data-react-props="{&quot;images&quot;:[{&quot;id&quot;:16,&quot;name&quot;:&quot;Ubuntu 22.04 LTS&quot;,&quot;aws_region&quot;:&quot;US East (N. Virginia)\t&quot;},{&quot;id&quot;:50,&quot;name&quot;:&quot;Ubuntu 18.04 LTS&quot;,&quot;aws_region&quot;:&quot;US East (N. Virginia)\t&quot;},{&quot;id&quot;:17,&quot;name&quot;:&quot;Ubuntu 22.04 LTS&quot;,&quot;aws_region&quot;:&quot;South America (São Paulo)&quot;},{&quot;id&quot;:51,&quot;name&quot;:&quot;Ubuntu 18.04 LTS&quot;,&quot;aws_region&quot;:&quot;South America (São Paulo)&quot;},{&quot;id&quot;:14,&quot;name&quot;:&quot;Ubuntu 22.04 LTS&quot;,&quot;aws_region&quot;:&quot;Europe (Paris)&quot;},{&quot;id&quot;:52,&quot;name&quot;:&quot;Ubuntu 18.04 LTS&quot;,&quot;aws_region&quot;:&quot;Europe (Paris)&quot;},{&quot;id&quot;:18,&quot;name&quot;:&quot;Ubuntu 22.04 LTS&quot;,&quot;aws_region&quot;:&quot;Asia Pacific (Sydney)&quot;},{&quot;id&quot;:53,&quot;name&quot;:&quot;Ubuntu 18.04 LTS&quot;,&quot;aws_region&quot;:&quot;Asia Pacific (Sydney)&quot;}],&quot;sandboxesUri&quot;:&quot;/user_sandboxes&quot;,&quot;csrfToken&quot;:&quot;t8unssjJ3yvMjhfYBSuQUha_AmGHk0wCC0rx7I51e1S_V9e-kJZPmti7ZIe6eZmVkqXcdgIokwi-irHI0sgTzQ&quot;,&quot;maxNumberOfContainers&quot;:2}" data-react-cache-id="user_sandboxes/Sandboxes-0"><div class="d-flex flex-column"><div class="dropdown pull-right" style="align-self: end;"><button aria-expanded="false" aria-haspopup="true" class="btn btn-lg btn-primary dropdown-toggle" data-toggle="dropdown" type="button">New sandbox <span class="caret"></span></button><ul class="dropdown-menu dropdown-menu-right"><li class="divider" role="separator"></li><li class="dropdown-header">US East (N. Virginia)	</li><li><a role="button">Ubuntu 18.04 LTS</a></li><li><a role="button">Ubuntu 22.04 LTS</a></li><li class="divider" role="separator"></li><li class="dropdown-header">South America (São Paulo)</li><li><a role="button">Ubuntu 18.04 LTS</a></li><li><a role="button">Ubuntu 22.04 LTS</a></li><li class="divider" role="separator"></li><li class="dropdown-header">Europe (Paris)</li><li><a role="button">Ubuntu 18.04 LTS</a></li><li><a role="button">Ubuntu 22.04 LTS</a></li><li class="divider" role="separator"></li><li class="dropdown-header">Asia Pacific (Sydney)</li><li><a role="button">Ubuntu 18.04 LTS</a></li><li><a role="button">Ubuntu 22.04 LTS</a></li></ul></div><div class="mt-2 alert alert-info">No sandboxes yet!</div></div></div></div></div></div></div>

      <div class="d-flex justify-content-around align-items-center">
          <div>
            <a data-toggle="tooltip" title="" class="btn btn-primary" role="button" href="/projects/2144" data-original-title="Advanced CSS">Previous project</a>
          </div>
          <form action="/corrections/877823/skip" method="post">
            <input name="authenticity_token" type="hidden" value="YMVSkUmM0Gr857SUR82G3KB2g1rLuGi3gcraRli9M7xoWSKdEdNA2-jSx8v4n48bJGxdTU4Dt700CppiBABbJQ">
            <button class="btn btn-warning" type="submit">
              Next project
            </button>
          </form>
      </div>
  </div>
</div>
