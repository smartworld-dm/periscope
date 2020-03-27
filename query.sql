select distinct b.memberid as Member_ID, 'https://ymcaatl.alariscloud.com/parse/files/EsvY4p2hTmRYM4xSob18OPvas5SPnmhYTDdLdjOT/'||signature  as image_url, b.firstname as child_first_name, b.lastname as child_last_name, to_char(b.birthdate, 'MM-DD-YYYY' ) AS birth_date,
case when signintype='STAFF' then coalesce(a.proxyfirstname, 'STAFF') else c.firstname end as adult_first_name,
case when signintype='STAFF' then coalesce(a.proxylastname, 'STAFF') else c.lastname end as adult_last_name,substring (a.eventtype, 7) as "Type",
TO_CHAR(convert_timezone('US/Eastern', a._created_at), 'MM-DD-YYYY HH:MM:SS' ) as "Time",  ymcaname as Facility, a.program__programname as programname, roomname as "Room",
'[' || 'Link to Image' || '](' ||'https://ymcaatl.alariscloud.com/parse/files/EsvY4p2hTmRYM4xSob18OPvas5SPnmhYTDdLdjOT/'||signature || ')' as signature
from atl_reporting.recordtable  a
left join atl_reporting.member b on 'Member$'||b._id= a._p_memberchild
left join atl_reporting.member c on coalesce('Member$'||c._id, 'STAFF')= coalesce(a._p_memberproxy, 'STAFF')
where eventtype in ('CHECK_IN', 'CHECK_OUT') 
and signature is not null
order by 2, 3, 4, 5, 6
limit 10