-- Find the description of the crime scene
SELECT description
FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28
AND street = 'Humphrey Street';
-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. Littering took place at 16:36. No known witnesses.

-- Finding the witnesses transcript
SELECT transcript
FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28
AND transcript LIKE "%bakery%";
-- 1. Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
-- 2. I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
-- 3. As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- 1. Finding security footage finding name with people with license plates
SELECT name
FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25
AND activity = 'exit';
-- Suspects: Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana Kelsey

-- 2. Finding who withdraw money from Leggett Street, common with suspects from first interview
SELECT name
FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'
AND name IN ('Vanessa', 'Bruce', 'Barry', 'Luca', 'Sofia', 'Iman', 'Diana Kelsey');
-- Common Suspects: Bruce, Iman, Luca

-- 3. Finding the first flight on the next day, and search from passengers
SELECT name, passengers.flight_id
FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
JOIN flights ON flights.id = passengers.flight_id
WHERE flights.year = 2021 AND flights.month = 7 AND flights.day = 29
AND flights.origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
AND name IN ('Bruce', 'Iman', 'Luca');
-- Common Suspects: Bruce, Luca - Flight ID 36

-- 3a. Finding the thief, his number and call id usint phone calls
SELECT people.name, people.phone_number, phone_calls.id
FROM people
JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
AND name IN ('Bruce', 'Luca');
-- THIEF FOUND CALLER: Bruce, CALL ID = 233

SELECT name, phone_number
FROM people
JOIN phone_calls ON phone_calls.receiver = people.phone_number
WHERE phone_calls.id = 233;
-- COMPLICE FOUND: Robin

-- Finding the city escaped to
SELECT city
FROM airports
JOIN flights ON flights.destination_airport_id = airports.id
WHERE flights.id = 36;
-- CITY FOUND: New York City
