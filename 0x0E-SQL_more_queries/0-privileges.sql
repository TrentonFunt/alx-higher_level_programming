-- List privileges of users user_0d_1 and user_0d_2
SELECT 
    user, 
    host, 
    db, 
    select_priv, 
    insert_priv, 
    update_priv, 
    delete_priv, 
    create_priv, 
    drop_priv, 
    grant_priv 
FROM 
    mysql.user 
WHERE 
    user IN ('user_0d_1', 'user_0d_2') 
    AND host = 'localhost';
