-- Отримати всі завдання певного користувача.
-- Використовуйте SELECT для отримання завдань конкретного користувача за його user_id.
select *
from tasks t
where t.user_id = 1;

-- Вибрати завдання за певним статусом.
-- Використовуйте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
select *
from tasks t 
where t.status_id = (select id from status where name = 'new');

-- Оновити статус конкретного завдання.
-- Змініть статус конкретного завдання на 'in progress' або інший статус.
update tasks
set status_id = (select id from status where name = 'completed')
where id = 19;

-- Отримати список користувачів, які не мають жодного завдання.
-- Використовуйте комбінацію SELECT, WHERE NOT IN і підзапит.
select u.*
from users u 
where u.id not in (
	select t.user_id 
	from tasks t
);

-- Додати нове завдання для конкретного користувача.
-- Використовуйте INSERT для додавання нового завдання.
insert into tasks (title, description, status_id, user_id)
values ('Create a report', 'Create a report of ... ', 1, 26);

-- Отримати всі завдання, які ще не завершено.
-- Виберіть завдання, чий статус не є 'завершено'.
select t.*
from tasks t 
where status_id <> (select id from status where name = 'completed');

-- Видалити конкретне завдання.
-- Використовуйте DELETE для видалення завдання за його id.
delete from tasks 
where id = 2546;

-- Знайти користувачів з певною електронною поштою.
-- Використовуйте SELECT із умовою LIKE для фільтрації за електронною поштою.
select u.*
from users u 
where u.email like 'bhansen@example.org';

-- Оновити ім'я користувача.
-- Змініть ім'я користувача за допомогою UPDATE.
update users 
set fullname = 'John Smith'
where id = 1000;

-- Отримати кількість завдань для кожного статусу.
-- Використовуйте SELECT, COUNT, GROUP BY для групування завдань за статусами.
select t.status_id, count(t.id) as count_of_tasks
from tasks t
group by t.status_id;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
-- Використовуйте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
select t.*, u.email as user_email
from tasks t 
join users u on u.id = t.user_id
where u.email like '%@example.org';

-- Отримати список завдань, що не мають опису.
-- Виберіть завдання, у яких відсутній опис.
select t.*
from tasks t 
where t.description is null;

-- Отримати користувачів та їхні завдання, які є у статусі 'in progress'.
-- Використовуйте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
select t.user_id, u.fullname, u.email, t.id as task_id, t.title, t.description, t.status_id  
from users u 
inner join tasks t on t.user_id = u.id 
where t.status_id = (select id from status where name = 'in progress');

-- Отримати користувачів та кількість їхніх завдань.
-- Використовуйте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
select u.id, u.fullname, u.email, COUNT(t.id) as count_of_tasks
from users u 
left join tasks t on t.user_id = u.id 
group by u.id, u.fullname, u.email;
