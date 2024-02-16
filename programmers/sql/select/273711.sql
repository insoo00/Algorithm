#1
select item_id, item_name, rarity
from item_info
where item_id in (
    select item_id from item_tree
        where parent_item_id in (select item_id from item_info where rarity = 'rare')
    )
order by item_id desc;

#2
select item_id, item_name, rarity
from item_info
where item_id in (
    select it.item_id
    from item_info as ii
    left join item_tree as it on ii.item_id = it.parent_item_id
    where ii.rarity='rare' and it.item_id is not null
    )
order by item_id desc;