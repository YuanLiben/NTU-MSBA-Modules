-- Q1 Retrieve a list of the names of participants. 
delimiter $$
create procedure q1()
begin
	select Name
	from participant;
end
$$ delimiter ;
call q1();

-- Q2 List the names of all participants who have enrolled in more than 2 weekly challenges. 
delimiter $$
create procedure q2()
begin
	select Name
	from participant
	where ParticipantID in
	(select ParticipantID
	from `participant-weeklychallenge`
	group by ParticipantID
	having count(WeeklyChallengeID) > 2);
end
$$ delimiter ;
call q2();

-- Q3 What is the number of participants who have redeemed at least one “Car Wash at Caltex”? 
delimiter $$
create procedure q3()
begin
	select count(distinct(ParticipantID)) as PartAmt
	from redemption 
	where RewardID = (select RewardID from reward where RewardName = 'Car Wash at Caltex')
	group by ParticipantID 
	having count(*) >= 1;
end
$$ delimiter ;
call q3();

-- Q4 List the names of participants who have accumulated more than 10,000 SC points and have redeemed at least one “Car Wash at Caltex”? 
delimiter $$
create procedure q4()
begin
	select Name 
	from participant
	where ParticipantID in
	(select ParticipantID
	from redemption 
	where RewardID = (select RewardID from reward where RewardName = 'Car Wash at Caltex')
	group by ParticipantID 
	having count(*) >= 1)
	and ParticipantID in
	(select participantID
	from (select ParticipantID, (sumbns+sumbsc) as sum
	from (select ParticipantID, sum(BonusAmt) as sumbns
	from `participant-weeklychallenge`
	natural join weeklychallenge
	where Status = 'Completed'
	group by ParticipantID) as bonus
	natural join
	(select ParticipantID, sum(BasicPointsEarned) as sumbsc
	from scpoint
	group by ParticipantID) as basic
	order by ParticipantID) as total
	where sum > 10000);
end
$$ delimiter ;
call q4();
/* Prof, for this question, I found that if combined basic sc points earned with sc points earned
in the weekly challenge, Ben accumulated more than 10000 sc points and was also satisfied the 
redeem requirement. So I write my query above and don't get the same result as in your sample 
output. Maybe I can discuss this question with you in this week's class? */