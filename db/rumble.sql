PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "player" ("id" INTEGER NOT NULL PRIMARY KEY, "discord_id" INTEGER NOT NULL, "name" VARCHAR(255) NOT NULL, "strength" INTEGER NOT NULL, "health" INTEGER NOT NULL, "last_workout" DATETIME NOT NULL);
CREATE UNIQUE INDEX "player_discord_id" ON "player" ("discord_id");
COMMIT;
