SELECT * FROM Planet
WHERE STATUS != 'CONFIRMED' OR radius < 0;

UPDATE Planet
SET kepler_name = NULL
WHERE STATUS != 'CONFIRMED';

DELETE FROM Planet
WHERE radius < 0;