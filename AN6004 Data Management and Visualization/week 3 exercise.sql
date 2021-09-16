use socialgram;
-- Q1
select name 
from user
where UserID in (
select UserID
from `user-group`
where isModerator = 'Y');

-- Q2
select name
from user
where UserID in (
select UserID
from `user-group`
group by UserID
having sum(isBanned = 'Y')>1);

-- Q3
select name, sum(filesize) as Total_Photo_Filesize
from user
natural join `user-photo` as uni
left outer join photo
on uni.PhotoID = photo.photoid
group by UserID
having sum(filesize) > 1000;

-- Q4
select AlbumName as Albumname, count(distinct(UserID)) as total_users
from album
where PhotoID
in (select PhotoID from album group by PhotoID having count(distinct(UserID))> 1) 
group by AlbumID;

-- Q5
select unify.UserID as userid, u1.name as userName, unify.FollowingUserID as following_userid, u2.name as following_userName
from (select user1.UserID, user1.FollowingUserID
from `user-following` as user1
left outer join `user-following` as user2
on user1.UserID = user2.FollowingUserID
where user2.UserID = user1.FollowingUserID) as unify
left outer join user u1
on unify.UserID = u1.UserID
left outer join user u2
on unify.FollowingUserID = u2.UserID;

-- Q6
select u1.name as User1, u2.name as User2, u3.name as User3
from (select user1.UserID as uid1, user2.UserID as uid2, user3.UserID as uid3
from `user-following` as user1
left outer join `user-following` as user2
on user1.FollowingUserID = user2.UserID
left outer join `user-following` as user3
on user2.FollowingUserID = user3.UserID
where user3.FollowingUserID = user1.UserID) as unify
left outer join user u1
on unify.uid1 = u1.UserID
left outer join user u2
on unify.uid2 = u2.UserID
left outer join user u3
on unify.uid3 = u3.UserID;
