db.createUser({
    user: 'my_user',
    pwd: 'my_pwd',
    roles: [
      {
        role: 'readWrite',
        db: 'my_db'
      },
    ],
  });
