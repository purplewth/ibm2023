SELECT o.owner_id, o.owner_name, COUNT(DISTINCT category_id) different_category_count
FROM owner o
LEFT JOIN article a
ON o.owner_id = a.owner_id
LEFT JOIN category_article_mapping m
ON a.article_id = m.article_id
LEFT JOIN category c
ON m.category_id = c.category_id
GROUP BY o.owner_id
ORDER BY different_category_count desc;
