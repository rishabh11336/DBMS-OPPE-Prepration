Week 2: Practice Question 1
```
select managers.name from managers, teams where teams.name = 'All Stars' and teams.team_id = managers.team_id
```

Week 2: Practice Question 2
```
select name from teams
```

Week 2: Practice Question 3
```
select book_catalogue.title from book_catalogue, book_authors where book_authors.isbn_no = book_catalogue.isbn_no and book_authors.author_fname='Joh Paul' and book_authors.author_lname='Mueller'
```

Week 2: Practice Question 4
```
select title from book_catalogue where publisher = 'McGraw Hill Education'
```

Week 2: Practice Question 5
```
select student_fname, student_lname from students where degree = 'M%'
```