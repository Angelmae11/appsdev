<?php

class crudDao {
    private $pdo;

    public function __construct(PDO $pdo) {

    }

   public function create($lastname, $fistname, $username, $password_hash, $email){
    $sql = "INSERT INTO tbsignup(lastname, firstname, username, password_hash, email)
            VALUES (:lastname, :firstname, :username, :password_hash, :email)";
    try {
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute([
           ':lastname'       => $lastname,
           ':firstname'      => $fistname,
           ':username'       => $username,
           ':password_hash'  => $password_hash,
           ':email'          => $email
        ]);
        return true;
    } catch (PDOException $e) {
        return $e->getMessage();
    }
}
public function login($identifier, $password) {
    $sql = "SELECT * FROM tbsignup
            WHERE username = :identifier OR email = :identifier
            LIMIT 1";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute([':identifier' => $identifier]);
            $user = $stmt->fetch(PDO::FETCH_ASSOC);

            if ($user && password_verify($password, $user['password-hash'])) {
                unset($user['password_hash']);
                return $user;
            }
            return false;
        } catch (PDOException $e) {
            return false;
        }
}
}