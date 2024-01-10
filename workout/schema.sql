DROP TABLE  IF EXISTS "user";
DROP TABLE  IF EXISTS "workout";

CREATE TABLE 'user' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'name' TEXT NOT NULL,
    'email' TEXT NOT NULL,
    'password' TEXT NOT NULL
);  

CREATE TABLE "workout" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "user_id" INTEGER NOT NULL,
    "date" DATE NOT NULL,
    "workout_name" TEXT NOT NULL,
    "sets" INTEGER NOT NULL,
    "reps" INTEGER NOT NULL,
    "weight" REAL NOT NULL,
    FOREIGN KEY ("user_id") REFERENCES "user"("id")
);
