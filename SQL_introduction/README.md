  <div class="panel-body">
    <p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/272/rtcwz.jpg" alt="" loading="lazy" style=""></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/jRAhwW4u4YvZtLtMGU2_6g" title="What is Database &amp; SQL?" target="_blank">What is Database &amp; SQL?</a> </li>
<li><a href="/rltoken/s3m_emsaSthyY041Wacgxg" title="Install MySQL (MySQL Server)" target="_blank">Install MySQL (MySQL Server)</a></li>
<li><a href="/rltoken/m_0RMf4RcC5NrHyjY1xN3w" title="A Basic MySQL Tutorial" target="_blank">A Basic MySQL Tutorial</a> </li>
<li><a href="/rltoken/-Qrnbp5eKmo7ajPDZekjfg" title="Basic SQL statements: DDL and DML" target="_blank">Basic SQL statements: DDL and DML</a> (<em>no need to read the chapter “Privileges”</em>)</li>
<li><a href="/rltoken/wXN5s1qexSTMh--NkTF1_w" title="Basic queries: SQL and RA" target="_blank">Basic queries: SQL and RA</a> </li>
<li><a href="/rltoken/7khGjnehvjHnqNZ9yizggg" title="SQL technique: functions" target="_blank">SQL technique: functions</a> </li>
<li><a href="/rltoken/xnJcopQTZyUke3LdAkOwow" title="SQL technique: subqueries" target="_blank">SQL technique: subqueries</a> </li>
<li><a href="/rltoken/QEr3XcBPhIR-E8NSSn1nzg" title="What makes the big difference between a backtick and an apostrophe?" target="_blank">What makes the big difference between a backtick and an apostrophe?</a> </li>
<li><a href="/rltoken/DGejihlnOkkNq-qJFM15MA" title="MySQL Cheat Sheet" target="_blank">MySQL Cheat Sheet</a> </li>
<li><a href="/rltoken/ePNUeloWxfiXwec7HeKe7Q" title="MySQL 8.0 SQL Statement Syntax" target="_blank">MySQL 8.0 SQL Statement Syntax</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/6bUOgrGi5Yd_I65Jp9bAfg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What’s a database</li>
<li>What’s a relational database</li>
<li>What does SQL stand for</li>
<li>What’s MySQL</li>
<li>How to create a database in MySQL</li>
<li>What does <code>DDL</code> and <code>DML</code> stand for</li>
<li>How to <code>CREATE</code> or <code>ALTER</code> a table</li>
<li>How to <code>SELECT</code> data from a table</li>
<li>How to <code>INSERT</code>, <code>UPDATE</code> or <code>DELETE</code> data</li>
<li>What are <code>subqueries</code></li>
<li>How to use MySQL functions</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be executed on Ubuntu 20.04 LTS using <code>MySQL 8.0</code> (version 8.0.25)</li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>, <code>WHERE</code>…)</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Comments for your SQL file:</h3>

<pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>

<h3>Install MySQL 8.0 on Ubuntu 20.04 LTS</h3>

<pre><code>$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
</code></pre>

<p>Connect to your MySQL server:</p>

<pre><code>$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql&gt;
mysql&gt; quit
Bye
$
</code></pre>

<h3>Use the sandbox to run MySQL</h3>

<p><strong>In the container, credentials are <code>root/root</code></strong></p>

<ul>
<li>Ask for container <code>Ubuntu 20.04</code></li>
<li>Connect via SSH</li>
<li>OR connect via the Web terminal</li>
<li>In the container, you should start MySQL before playing with it:</li>
</ul>

<pre><code>$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$
</code></pre>

<p><strong>In the container, credentials are <code>root/root</code></strong></p>

  </div>
</div>




        <div class="panel panel-default" id="project-quiz-questions-title">
    <div class="panel-heading">
      <h3 class="panel-title">
        Quiz questions
      </h3>
    </div>

    <div class="panel-body">

        <div class="alert alert-info">
          <strong>Great!</strong>
          You've completed the quiz successfully! Keep going!
          <span id="quiz_questions_collapse_toggle">(Show quiz)</span>
        </div>

      <section class="quiz_questions_show_container" style="display: none;">
          <div class="quiz_question_item_container" data-role="quiz_question5525" data-position="1">
            <div class=" clearfix" id="quiz_question-5525">

    <h4 class="quiz_question">

        Question #0
    </h4>

    <!-- Quiz question Body -->
    <p>What does SQL stand for?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5525">
                <li class="">

  <input type="radio" name="5525" id="5525-1499182179009" value="1499182179009" data-quiz-answer-id="1499182179009" data-quiz-question-id="5525" disabled="disabled">
  <label for="5525-1499182179009"><p>Sequences of Query Logic</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5525" id="5525-1499182193195" value="1499182193195" data-quiz-answer-id="1499182193195" data-quiz-question-id="5525" disabled="disabled" checked="checked">
  <label for="5525-1499182193195"><p>Structured Query Language</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5525" id="5525-1499182208288" value="1499182208288" data-quiz-answer-id="1499182208288" data-quiz-question-id="5525" disabled="disabled">
  <label for="5525-1499182208288"><p>Solid Query Language</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5525" id="5525-1499182214593" value="1499182214593" data-quiz-answer-id="1499182214593" data-quiz-question-id="5525" disabled="disabled">
  <label for="5525-1499182214593"><p>Structured Question Language</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5526" data-position="2">
            <div class=" clearfix" id="quiz_question-5526">

    <h4 class="quiz_question">

        Question #1
    </h4>

    <!-- Quiz question Body -->
    <p>What is a relational database? (please select all correct answers)</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5526">
                <li class="">

  <input type="checkbox" name="5526" id="5526-1499182230199" value="1499182230199" data-quiz-answer-id="1499182230199" data-quiz-question-id="5526" disabled="disabled" checked="checked">
  <label for="5526-1499182230199"><p>a database</p>
</label>
</li>

                <li class="">

  <input type="checkbox" name="5526" id="5526-1499182260102" value="1499182260102" data-quiz-answer-id="1499182260102" data-quiz-question-id="5526" disabled="disabled" checked="checked">
  <label for="5526-1499182260102"><p>a collection of data</p>
</label>
</li>

                <li class="">

  <input type="checkbox" name="5526" id="5526-1499182314890" value="1499182314890" data-quiz-answer-id="1499182314890" data-quiz-question-id="5526" disabled="disabled">
  <label for="5526-1499182314890"><p>married databases</p>
</label>
</li>

                <li class="">

  <input type="checkbox" name="5526" id="5526-1499182335900" value="1499182335900" data-quiz-answer-id="1499182335900" data-quiz-question-id="5526" disabled="disabled" checked="checked">
  <label for="5526-1499182335900"><p>data are organized by tables, records and columns</p>
</label>
</li>

                <li class="">

  <input type="checkbox" name="5526" id="5526-1499182397720" value="1499182397720" data-quiz-answer-id="1499182397720" data-quiz-question-id="5526" disabled="disabled">
  <label for="5526-1499182397720"><p>data are organized by tables and indexes</p>
</label>
</li>

                <li class="">

  <input type="checkbox" name="5526" id="5526-1499182411653" value="1499182411653" data-quiz-answer-id="1499182411653" data-quiz-question-id="5526" disabled="disabled">
  <label for="5526-1499182411653"><p>a table containing multiple object representation </p>
</label>
</li>

                <li class="">

  <input type="checkbox" name="5526" id="5526-1499182545093" value="1499182545093" data-quiz-answer-id="1499182545093" data-quiz-question-id="5526" disabled="disabled" checked="checked">
  <label for="5526-1499182545093"><p>a table containing only one object representation</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5527" data-position="3">
            <div class=" clearfix" id="quiz_question-5527">

    <h4 class="quiz_question">

        Question #2
    </h4>

    <!-- Quiz question Body -->
    <p>What does DDL stand for?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5527">
                <li class="">

  <input type="radio" name="5527" id="5527-1499182722148" value="1499182722148" data-quiz-answer-id="1499182722148" data-quiz-question-id="5527" disabled="disabled" checked="checked">
  <label for="5527-1499182722148"><p>Data Definition Language</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5527" id="5527-1499182725423" value="1499182725423" data-quiz-answer-id="1499182725423" data-quiz-question-id="5527" disabled="disabled">
  <label for="5527-1499182725423"><p>Database Definition Language</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5527" id="5527-1499182731927" value="1499182731927" data-quiz-answer-id="1499182731927" data-quiz-question-id="5527" disabled="disabled">
  <label for="5527-1499182731927"><p>Data Document Language</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5527" id="5527-1499182752697" value="1499182752697" data-quiz-answer-id="1499182752697" data-quiz-question-id="5527" disabled="disabled">
  <label for="5527-1499182752697"><p>Document Data Language</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5528" data-position="4">
            <div class=" clearfix" id="quiz_question-5528">

    <h4 class="quiz_question">

        Question #3
    </h4>

    <!-- Quiz question Body -->
    <p>What does DML stand for?</p>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5528">
                <li class="">

  <input type="radio" name="5528" id="5528-1499182784481" value="1499182784481" data-quiz-answer-id="1499182784481" data-quiz-question-id="5528" disabled="disabled">
  <label for="5528-1499182784481"><p>Database Manipulation Language</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5528" id="5528-1499182796585" value="1499182796585" data-quiz-answer-id="1499182796585" data-quiz-question-id="5528" disabled="disabled">
  <label for="5528-1499182796585"><p>Document Manipulation Language</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5528" id="5528-1499182803652" value="1499182803652" data-quiz-answer-id="1499182803652" data-quiz-question-id="5528" disabled="disabled" checked="checked">
  <label for="5528-1499182803652"><p>Data Manipulation Language</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5528" id="5528-1499182808532" value="1499182808532" data-quiz-answer-id="1499182808532" data-quiz-question-id="5528" disabled="disabled">
  <label for="5528-1499182808532"><p>Document Model Language</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5529" data-position="5">
            <div class=" clearfix" id="quiz_question-5529">

    <h4 class="quiz_question">

        Question #4
    </h4>

    <!-- Quiz question Body -->
    <p>How do you list all <code>users</code> in this table?</p>

<pre><code>+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5529">
                <li class="">

  <input type="radio" name="5529" id="5529-1499182885566" value="1499182885566" data-quiz-answer-id="1499182885566" data-quiz-question-id="5529" disabled="disabled">
  <label for="5529-1499182885566"><p>DELETE * FROM users;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5529" id="5529-1499182894961" value="1499182894961" data-quiz-answer-id="1499182894961" data-quiz-question-id="5529" disabled="disabled" checked="checked">
  <label for="5529-1499182894961"><p>SELECT * FROM users;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5529" id="5529-1499182898045" value="1499182898045" data-quiz-answer-id="1499182898045" data-quiz-question-id="5529" disabled="disabled">
  <label for="5529-1499182898045"><p>SELECT ALL users;</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5530" data-position="6">
            <div class=" clearfix" id="quiz_question-5530">

    <h4 class="quiz_question">

        Question #5
    </h4>

    <!-- Quiz question Body -->
    <p>How to you add a new record in the table <code>users</code>?</p>

<pre><code>+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5530">
                <li class="">

  <input type="radio" name="5530" id="5530-1499182935742" value="1499182935742" data-quiz-answer-id="1499182935742" data-quiz-question-id="5530" disabled="disabled">
  <label for="5530-1499182935742"><p>INSERT users (id, name, age) VALUES (2, “Betty”, 30);</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5530" id="5530-1499182985004" value="1499182985004" data-quiz-answer-id="1499182985004" data-quiz-question-id="5530" disabled="disabled">
  <label for="5530-1499182985004"><p>INSERT INTO users (id, name) VALUES (2, “Betty”, 30);</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5530" id="5530-1499182988458" value="1499182988458" data-quiz-answer-id="1499182988458" data-quiz-question-id="5530" disabled="disabled" checked="checked">
  <label for="5530-1499182988458"><p>INSERT INTO users (id, name, age) VALUES (2, “Betty”, 30);</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5530" id="5530-1499183015319" value="1499183015319" data-quiz-answer-id="1499183015319" data-quiz-question-id="5530" disabled="disabled">
  <label for="5530-1499183015319"><p>INSERT INTO users (id, name, age) VALUES (2, “Betty”);</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5531" data-position="7">
            <div class=" clearfix" id="quiz_question-5531">

    <h4 class="quiz_question">

        Question #6
    </h4>

    <!-- Quiz question Body -->
    <p>How do you delete the <code>users</code> record with <code>id = 89</code> in this table?</p>

<pre><code>+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5531">
                <li class="">

  <input type="radio" name="5531" id="5531-1499183023305" value="1499183023305" data-quiz-answer-id="1499183023305" data-quiz-question-id="5531" disabled="disabled">
  <label for="5531-1499183023305"><p>DELETE users WHERE id = 89;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5531" id="5531-1499183060780" value="1499183060780" data-quiz-answer-id="1499183060780" data-quiz-question-id="5531" disabled="disabled" checked="checked">
  <label for="5531-1499183060780"><p>DELETE FROM users WHERE id = 89;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5531" id="5531-1499183062965" value="1499183062965" data-quiz-answer-id="1499183062965" data-quiz-question-id="5531" disabled="disabled">
  <label for="5531-1499183062965"><p>DELETE FROM users;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5531" id="5531-1499183072862" value="1499183072862" data-quiz-answer-id="1499183072862" data-quiz-question-id="5531" disabled="disabled">
  <label for="5531-1499183072862"><p>DELETE FROM users WHERE id IS EQUAL TO 89;</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5532" data-position="8">
            <div class=" clearfix" id="quiz_question-5532">

    <h4 class="quiz_question">

        Question #7
    </h4>

    <!-- Quiz question Body -->
    <p>How do you change the name of the <code>users</code> record with <code>id = 89</code> to <code>Holberton</code>?</p>

<pre><code>+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5532">
                <li class="">

  <input type="radio" name="5532" id="5532-1499183092125" value="1499183092125" data-quiz-answer-id="1499183092125" data-quiz-question-id="5532" disabled="disabled" checked="checked">
  <label for="5532-1499183092125"><p>UPDATE users SET name = “Holberton” WHERE id = 89;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5532" id="5532-1499183140219" value="1499183140219" data-quiz-answer-id="1499183140219" data-quiz-question-id="5532" disabled="disabled">
  <label for="5532-1499183140219"><p>CHANGE users SET name = “Holberton” WHERE id = 89;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5532" id="5532-1499183143756" value="1499183143756" data-quiz-answer-id="1499183143756" data-quiz-question-id="5532" disabled="disabled">
  <label for="5532-1499183143756"><p>UPDATE users SET name = “Holberton”;</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>
          <div class="quiz_question_item_container" data-role="quiz_question5533" data-position="9">
            <div class=" clearfix" id="quiz_question-5533">

    <h4 class="quiz_question">

        Question #8
    </h4>

    <!-- Quiz question Body -->
    <p>How do you list all <code>users</code> records with <code>age &gt; 21</code> in this table?</p>

<pre><code>+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
</code></pre>


    <!-- Quiz question Answers -->
        <ul class="quiz_question_answers" data-question-id="5533">
                <li class="">

  <input type="radio" name="5533" id="5533-1499183214708" value="1499183214708" data-quiz-answer-id="1499183214708" data-quiz-question-id="5533" disabled="disabled">
  <label for="5533-1499183214708"><p>SELECT * FROM users WHERE age &lt; 21;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5533" id="5533-1499183230443" value="1499183230443" data-quiz-answer-id="1499183230443" data-quiz-question-id="5533" disabled="disabled">
  <label for="5533-1499183230443"><p>SELECT * FROM users WHERE age IS UP TO 21;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5533" id="5533-1499183232591" value="1499183232591" data-quiz-answer-id="1499183232591" data-quiz-question-id="5533" disabled="disabled" checked="checked">
  <label for="5533-1499183232591"><p>SELECT * FROM users WHERE age &gt; 21;</p>
</label>
</li>

                <li class="">

  <input type="radio" name="5533" id="5533-1499183254189" value="1499183254189" data-quiz-answer-id="1499183254189" data-quiz-question-id="5533" disabled="disabled">
  <label for="5533-1499183254189"><p>SELECT * FROM users WHERE age BETWEEN 21 AND 89;</p>
</label>
</li>

        </ul>

    <!-- Quiz question Tips -->

</div>

          </div>

      </section>
    </div>
  </div>



          <h2 class="gap">Tasks</h2>

    <div data-role="task19512" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-19512">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. List databases
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
    <p>Write a script that lists all databases of your MySQL server.</p>

<pre><code>guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
sys
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>0-list_databases.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19512" data-batch-id="558" data-toggle="modal" data-target="#task-19512-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19512-users-done-modal" data-task-id="19512" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "0. List databases"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19512-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19513" data-position="2" id="task-num-1">
      <div class="panel panel-default task-card " id="task-19513">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Create a database
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
    <p>Write a script that creates the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>If the database <code>hbtn_0c_0</code> already exists, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>1-create_database_if_missing.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19513" data-batch-id="558" data-toggle="modal" data-target="#task-19513-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19513-users-done-modal" data-task-id="19513" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "1. Create a database"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19513-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19514" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-19514">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Delete a database
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
    <p>Write a script that deletes the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>If the database <code>hbtn_0c_0</code> doesn’t exist, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
hbtn_0c_0
information_schema
mysql
performance_schema
sys
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
sys
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>2-remove_database.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19514" data-batch-id="558" data-toggle="modal" data-target="#task-19514-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19514-users-done-modal" data-task-id="19514" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "2. Delete a database"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19514-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19515" data-position="4" id="task-num-3">
      <div class="panel panel-default task-card " id="task-19515">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. List tables
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
    <p>Write a script that lists all the tables of a database in your MySQL server.</p>

<ul>
<li>The database name will be passed as argument of <code>mysql</code> command (in the following example: <code>mysql</code> is the name of the database)</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password:
Tables_in_mysql
columns_priv
component
db
default_roles
engine_cost
func
general_log
global_grants
gtid_executed
help_category
help_keyword
help_relation
help_topic
innodb_index_stats
innodb_table_stats
password_history
plugin
procs_priv
proxies_priv
replication_asynchronous_connection_failover
replication_asynchronous_connection_failover_managed
role_edges
server_cost
servers
slave_master_info
slave_relay_log_info
slave_worker_info
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>3-list_tables.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19515" data-batch-id="558" data-toggle="modal" data-target="#task-19515-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19515-users-done-modal" data-task-id="19515" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "3. List tables"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19515-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19516" data-position="5" id="task-num-4">
      <div class="panel panel-default task-card " id="task-19516">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      4. First table
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
    <p>Write a script that creates a table called <code>first_table</code> in the current database in your MySQL server.</p>

<ul>
<li><code>first_table</code> description:

<ul>
<li><code>id</code> INT</li>
<li><code>name</code> VARCHAR(256)</li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>If the table <code>first_table</code> already exists, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>4-first_table.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19516" data-batch-id="558" data-toggle="modal" data-target="#task-19516-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19516-users-done-modal" data-task-id="19516" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "4. First table"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19516-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19517" data-position="6" id="task-num-5">
      <div class="panel panel-default task-card " id="task-19517">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      5. Full description
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
    <p>Write a script that prints the following description of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
<li>You are not allowed to use the <code>DESCRIBE</code> or <code>EXPLAIN</code> statements</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
Table   Create Table
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>5-full_table.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19517" data-batch-id="558" data-toggle="modal" data-target="#task-19517-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19517-users-done-modal" data-task-id="19517" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "5. Full description"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19517-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19518" data-position="7" id="task-num-6">
      <div class="panel panel-default task-card " id="task-19518">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      6. List all in table
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
    <p>Write a script that lists all rows of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>All fields should be printed</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>6-list_values.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19518" data-batch-id="558" data-toggle="modal" data-target="#task-19518-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19518-users-done-modal" data-task-id="19518" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "6. List all in table"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19518-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19519" data-position="8" id="task-num-7">
      <div class="panel panel-default task-card " id="task-19519">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      7. First add
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
    <p>Write a script that inserts a new row in the table <code>first_table</code> (database <code>hbtn_0c_0</code>) in your MySQL server.</p>

<ul>
<li>New row:

<ul>
<li><code>id</code> = <code>89</code></li>
<li><code>name</code> = <code>Best School</code></li>
</ul></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
id  name
89  Best School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
id  name
89  Best School
89  Best School
89  Best School
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>7-insert_value.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19519" data-batch-id="558" data-toggle="modal" data-target="#task-19519-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19519-users-done-modal" data-task-id="19519" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "7. First add"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19519-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19520" data-position="9" id="task-num-8">
      <div class="panel panel-default task-card " id="task-19520">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      8. Count 89
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
    <p>Write a script that displays the number of records with <code>id = 89</code> in the table <code>first_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password:
3
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>8-count_89.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19520" data-batch-id="558" data-toggle="modal" data-target="#task-19520-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19520-users-done-modal" data-task-id="19520" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "8. Count 89"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19520-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19521" data-position="10" id="task-num-9">
      <div class="panel panel-default task-card " id="task-19521">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      9. Full creation
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
    <p>Write a script that creates a table <code>second_table</code> in the database <code>hbtn_0c_0</code> in your MySQL server and add multiples rows.</p>

<ul>
<li><code>second_table</code> description:

<ul>
<li><code>id</code> INT</li>
<li><code>name</code> VARCHAR(256)</li>
<li><code>score</code> INT</li>
</ul></li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>
<li>If the table <code>second_table</code> already exists, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> and <code>SHOW</code> statements</li>
<li>Your script should create these records:

<ul>
<li><code>id</code> = 1, <code>name</code> = “John”, <code>score</code> = 10</li>
<li><code>id</code> = 2, <code>name</code> = “Alex”, <code>score</code> = 3</li>
<li><code>id</code> = 3, <code>name</code> = “Bob”, <code>score</code> = 14</li>
<li><code>id</code> = 4, <code>name</code> = “George”, <code>score</code> = 8</li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>9-full_creation.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19521" data-batch-id="558" data-toggle="modal" data-target="#task-19521-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19521-users-done-modal" data-task-id="19521" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "9. Full creation"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19521-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19522" data-position="11" id="task-num-10">
      <div class="panel panel-default task-card " id="task-19522">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      10. List by best
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
    <p>Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>Results should display both the score and the name (in this order)</li>
<li>Records should be ordered by score (top first) </li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>10-top_score.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19522" data-batch-id="558" data-toggle="modal" data-target="#task-19522-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19522-users-done-modal" data-task-id="19522" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "10. List by best"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19522-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19523" data-position="12" id="task-num-11">
      <div class="panel panel-default task-card " id="task-19523">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      11. Select the best
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
    <p>Write a script that lists all records with a <code>score &gt;= 10</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>Results should display both the score and the name (in this order)</li>
<li>Records should be ordered by score (top first)</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
14  Bob
10  John
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>11-best_score.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19523" data-batch-id="558" data-toggle="modal" data-target="#task-19523-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19523-users-done-modal" data-task-id="19523" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "11. Select the best"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19523-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19524" data-position="13" id="task-num-12">
      <div class="panel panel-default task-card " id="task-19524">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      12. Cheating is bad
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
    <p>Write a script that updates the score of Bob to <code>10</code> in the table <code>second_table</code>.</p>

<ul>
<li>You are not allowed to use Bob’s id value, only the <code>name</code> field</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>12-no_cheating.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19524" data-batch-id="558" data-toggle="modal" data-target="#task-19524-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19524-users-done-modal" data-task-id="19524" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "12. Cheating is bad"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19524-score-info-score">0</span>/8
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19525" data-position="14" id="task-num-13">
      <div class="panel panel-default task-card " id="task-19525">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      13. Score too low
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
    <p>Write a script that removes all records with a <code>score &lt;= 5</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>13-change_class.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19525" data-batch-id="558" data-toggle="modal" data-target="#task-19525-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19525-users-done-modal" data-task-id="19525" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "13. Score too low"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19525-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19526" data-position="15" id="task-num-14">
      <div class="panel panel-default task-card " id="task-19526">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      14. Average
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
    <p>Write a script that computes the score average of all records in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>The result column name should be <code>average</code></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
average
9.3333
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>14-average.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19526" data-batch-id="558" data-toggle="modal" data-target="#task-19526-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19526-users-done-modal" data-task-id="19526" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "14. Average"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19526-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19527" data-position="16" id="task-num-15">
      <div class="panel panel-default task-card " id="task-19527">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      15. Number by score
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
    <p>Write a script that lists the number of records with the same score in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>The result should display:

<ul>
<li>the <code>score</code></li>
<li>the number of records for this <code>score</code> with the label <code>number</code></li>
</ul></li>
<li>The list should be sorted by the number of records (descending)</li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>
</ul>

<pre><code>guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   number
10  2
8   1
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>15-groups.sql</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">

<div>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="19527" data-batch-id="558" data-toggle="modal" data-target="#task-19527-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-19527-users-done-modal" data-task-id="19527" data-batch-id="558">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
            <h4 class="modal-title">Students who are done with "15. Number by score"</h4>
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




    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#sandboxes-modal"><i aria-hidden="true" class="fa fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
            <strong class="text-primary">
              <span id="task-19527-score-info-score">0</span>/6
            </strong>
            <span class="text-muted">pts</span>
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task19528" data-position="17" id="task-num-16">
      <div class="panel panel-default task-card " id="task-19528">
  <span id="user_id" data-id="8687"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      16. Say my name
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
    <p>Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<ul>
<li>Don’t list rows without a <code>name</code> value</li>
<li>Results should display the score and the name (in this order)</li>
<li>Records should be listed by descending score </li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>
</ul>

<p>In this example, new data have been added to the table <code>second_table</code>.</p>

<pre><code>guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Technical information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
            <li>Directory: <code>SQL_introduction</code></li>
            <li>File: <code>16-no_link.sql</code></li>
        </ul>
      </div>

    <!
