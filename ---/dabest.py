
import sqlite3

connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
cursor = connection.cursor()

def insert_players():
    import sqlite3

    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO players (player_id, team_id, player_name, player_image_path, button_id, button_object_name, player_number, player_height, player_weight, player_birthday, player_status, student_id, thai_id, phone_number)
    VALUES
    (1, 1, 'Ian Mehta', 'C:/players/team1/Screenshot 2025-08-24 222800.png', 1, 'C:/players/team1/Screenshot 2025-08-24 222800.png', '90', 195, 61, '28 / 07 / 2003', 'Undergraduate', '6638195875', '1417147649111', '0657379022'),
    (2, 1, 'Silas Lim', 'C:/players/team1/Screenshot 2025-08-24 222805.png', 2, 'C:/players/team1/Screenshot 2025-08-24 222805.png', '92', 191, 82, '13 / 10 / 2003', 'Undergraduate', '6599952792', '1380889736311', '0982996907'),
    (3, 1, 'Dana Nolan', 'C:/players/team1/Screenshot 2025-08-24 222825.png', 3, 'C:/players/team1/Screenshot 2025-08-24 222825.png', '42', 156, 62, '28 / 05 / 2003', 'Undergraduate', '6780912955', '1414110932704', '0688606058'),
    (4, 1, 'Riley Fuller', 'C:/players/team1/Screenshot 2025-08-24 222831.png', 4, 'C:/players/team1/Screenshot 2025-08-24 222831.png', '03', 165, 77, '06 / 10 / 2004', 'Undergraduate', '6630242617', '1375064230155', '0931229801'),
    (5, 1, 'Miles Wong', 'C:/players/team1/Screenshot 2025-08-24 222837.png', 5, 'C:/players/team1/Screenshot 2025-08-24 222837.png', '08', 173, 81, '07 / 08 / 2003', 'Undergraduate', '6769152496', '2351612723865', '0947407231'),
    (6, 1, 'Emma Barker', 'C:/players/team1/Screenshot 2025-08-24 222843.png', 6, 'C:/players/team1/Screenshot 2025-08-24 222843.png', '24', 187, 53, '17 / 03 / 2004', 'Undergraduate', '6768459390', '2427251679372', '0945392181'),
    (7, 1, 'Elias Evans', 'C:/players/team1/Screenshot 2025-08-24 222850.png', 7, 'C:/players/team1/Screenshot 2025-08-24 222850.png', '53', 188, 92, '17 / 11 / 2003', 'Undergraduate', '6680924298', '2358379513596', '0843925039'),
    (8, 1, 'Naomi Brooks', 'C:/players/team1/Screenshot 2025-08-24 222855.png', 8, 'C:/players/team1/Screenshot 2025-08-24 222855.png', '38', 158, 76, '28 / 05 / 2004', 'Undergraduate', '6558792321', '2480063662879', '0872912481'),
    (9, 1, 'Reese Larson', 'C:/players/team1/Screenshot 2025-08-24 222901.png', 9, 'C:/players/team1/Screenshot 2025-08-24 222901.png', '97', 156, 61, '19 / 02 / 2003', 'Undergraduate', '6571679289', '2339029226726', '0918051322'),
    (10, 1, 'Caleb Barnes', 'C:/players/team1/Screenshot 2025-08-24 222907.png', 10, 'C:/players/team1/Screenshot 2025-08-24 222907.png', '61', 192, 92, '30 / 05 / 2004', 'Undergraduate', '6563015624', '2484071972273', '0950464144'),
    (11, 1, 'Ian Price', 'C:/players/team1/Screenshot 2025-08-24 222915.png', 11, 'C:/players/team1/Screenshot 2025-08-24 222915.png', '88', 173, 91, '06 / 06 / 2003', 'Undergraduate', '6729542090', '2492963445990', '0897740501'),
    (12, 1, 'Violet Miller', 'C:/players/team1/Screenshot 2025-08-24 222920.png', 12, 'C:/players/team1/Screenshot 2025-08-24 222920.png', '05', 187, 53, '25 / 07 / 2003', 'Undergraduate', '6692715241', '2448578196786', '0919249309'),
    (13, 2, 'Zayne Edwards', 'C:/players/team2/Screenshot 2025-08-24 223234.png', 1, 'C:/players/team2/Screenshot 2025-08-24 223234.png', '35', 176, 82, '28 / 08 / 2004', 'Undergraduate', '6629133622', '1302983408898', '0981837375'),
    (14, 2, 'Jonah Tan', 'C:/players/team2/Screenshot 2025-08-24 223247.png', 2, 'C:/players/team2/Screenshot 2025-08-24 223247.png', '86', 193, 90, '09 / 02 / 2004', 'Undergraduate', '6696441915', '2301394915067', '0908923931'),
    (15, 2, 'Parker Johns', 'C:/players/team2/Screenshot 2025-08-24 223251.png', 3, 'C:/players/team2/Screenshot 2025-08-24 223251.png', '76', 159, 83, '05 / 11 / 2004', 'Undergraduate', '6781880392', '1421548307399', '0842241547'),
    (16, 2, 'Sawyer Reed', 'C:/players/team2/Screenshot 2025-08-24 223259.png', 4, 'C:/players/team2/Screenshot 2025-08-24 223259.png', '62', 174, 97, '23 / 12 / 2004', 'Undergraduate', '6700216261', '1393961065808', '0600740083'),
    (17, 2, 'Wren Cohen', 'C:/players/team2/Screenshot 2025-08-24 223306.png', 5, 'C:/players/team2/Screenshot 2025-08-24 223306.png', '29', 199, 53, '18 / 11 / 2004', 'Undergraduate', '6521987478', '1347824141891', '0845461497'),
    (18, 2, 'Dominic D''''Angelo', 'C:/players/team2/Screenshot 2025-08-24 223312.png', 6, 'C:/players/team2/Screenshot 2025-08-24 223312.png', '67', 194, 98, '07 / 05 / 2003', 'Undergraduate', '6575338687', '1420326312531', '0863859360'),
    (19, 2, 'Yosef Reed', 'C:/players/team2/Screenshot 2025-08-24 223317.png', 7, 'C:/players/team2/Screenshot 2025-08-24 223317.png', '28', 177, 89, '19 / 11 / 2004', 'Undergraduate', '6622680166', '1359950960164', '0982930485'),
    (20, 2, 'Omar Clark', 'C:/players/team2/Screenshot 2025-08-24 223322.png', 8, 'C:/players/team2/Screenshot 2025-08-24 223322.png', '52', 167, 73, '15 / 08 / 2005', 'Undergraduate', '6547384219', '1361823743523', '0665066385'),
    (21, 2, 'Blair Rossi', 'C:/players/team2/Screenshot 2025-08-24 223327.png', 9, 'C:/players/team2/Screenshot 2025-08-24 223327.png', '78', 161, 55, '12 / 08 / 2004', 'Undergraduate', '6688058931', '1340866558549', '0810921524'),
    (22, 2, 'Adrian Xu', 'C:/players/team2/Screenshot 2025-08-24 223332.png', 10, 'C:/players/team2/Screenshot 2025-08-24 223332.png', '80', 196, 83, '14 / 10 / 2005', 'Undergraduate', '6770743074', '1454343684070', '0998502417'),
    (23, 2, 'Levi Ueda', 'C:/players/team2/Screenshot 2025-08-24 223338.png', 11, 'C:/players/team2/Screenshot 2025-08-24 223338.png', '49', 185, 92, '16 / 07 / 2004', 'Undergraduate', '6731866241', '1450831683320', '0962439916'),
    (24, 2, 'Jade Simmons', 'C:/players/team2/Screenshot 2025-08-24 223341.png', 12, 'C:/players/team2/Screenshot 2025-08-24 223341.png', '31', 166, 95, '01 / 10 / 2004', 'Undergraduate', '6543789189', '2448105929778', '0972892948'),
    (25, 3, 'Tessa D''''Angelo', 'C:/players/team3/Screenshot 2025-08-24 223446.png', 1, 'C:/players/team3/Screenshot 2025-08-24 223446.png', '17', 155, 74, '09 / 02 / 2003', 'Undergraduate', '6506953189', '1443718069746', '0671640221'),
    (26, 3, 'Sawyer Cole', 'C:/players/team3/Screenshot 2025-08-24 223452.png', 2, 'C:/players/team3/Screenshot 2025-08-24 223452.png', '30', 159, 70, '30 / 07 / 2004', 'Undergraduate', '6772344427', '1427132941415', '0972230656'),
    (27, 3, 'Reese D''''Angelo', 'C:/players/team3/Screenshot 2025-08-24 223455.png', 3, 'C:/players/team3/Screenshot 2025-08-24 223455.png', '96', 189, 55, '02 / 12 / 2004', 'Undergraduate', '6524017088', '2408909165459', '0945994127'),
    (28, 3, 'Rowan Jones', 'C:/players/team3/Screenshot 2025-08-24 223502.png', 4, 'C:/players/team3/Screenshot 2025-08-24 223502.png', '25', 172, 74, '10 / 01 / 2004', 'Undergraduate', '6575571200', '1429701002827', '0892819598'),
    (29, 3, 'Omar Zhang', 'C:/players/team3/Screenshot 2025-08-24 223507.png', 5, 'C:/players/team3/Screenshot 2025-08-24 223507.png', '20', 195, 72, '12 / 06 / 2003', 'Undergraduate', '6610986432', '1341176264601', '0956762497'),
    (30, 3, 'Riley Lam', 'C:/players/team3/Screenshot 2025-08-24 223513.png', 6, 'C:/players/team3/Screenshot 2025-08-24 223513.png', '69', 176, 52, '29 / 09 / 2003', 'Undergraduate', '6581875709', '1487654410721', '0851649923'),
    (31, 3, 'Kai Reed', 'C:/players/team3/Screenshot 2025-08-24 223518.png', 7, 'C:/players/team3/Screenshot 2025-08-24 223518.png', '24', 162, 66, '08 / 10 / 2004', 'Undergraduate', '6675228311', '1399036000471', '0972399420'),
    (32, 3, 'Nash Jenkins', 'C:/players/team3/Screenshot 2025-08-24 223522.png', 8, 'C:/players/team3/Screenshot 2025-08-24 223522.png', '77', 176, 75, '21 / 07 / 2003', 'Undergraduate', '6634337017', '1332403869835', '0938816566'),
    (33, 3, 'Jay Hughes', 'C:/players/team3/Screenshot 2025-08-24 223526.png', 9, 'C:/players/team3/Screenshot 2025-08-24 223526.png', '53', 187, 53, '08 / 02 / 2005', 'Undergraduate', '6737555491', '1489914560452', '0615286693'),
    (34, 3, 'Evan Fuller', 'C:/players/team3/Screenshot 2025-08-24 223529.png', 10, 'C:/players/team3/Screenshot 2025-08-24 223529.png', '22', 175, 90, '20 / 05 / 2004', 'Undergraduate', '6705165518', '1349337239570', '0929591249'),
    (35, 3, 'Paxton Ueda', 'C:/players/team3/Screenshot 2025-08-24 223534.png', 11, 'C:/players/team3/Screenshot 2025-08-24 223534.png', '39', 162, 90, '16 / 12 / 2004', 'Undergraduate', '6602048202', '1482029692993', '0817528152'),
    (36, 3, 'Vera Shaw', 'C:/players/team3/Screenshot 2025-08-24 223545.png', 12, 'C:/players/team3/Screenshot 2025-08-24 223545.png', '51', 180, 56, '19 / 09 / 2004', 'Undergraduate', '6732973450', '2356349860067', '0913275509'),
    (37, 4, 'Hunter Underwood', 'C:/players/team4/Screenshot 2025-08-25 004434.png', 1, 'C:/players/team4/Screenshot 2025-08-25 004434.png', '30', 194, 95, '19 / 01 / 2003', 'Undergraduate', '6737837469', '2408655793615', '0833446031'),
    (38, 4, 'Lena Bennett', 'C:/players/team4/Screenshot 2025-08-25 004437.png', 2, 'C:/players/team4/Screenshot 2025-08-25 004437.png', '91', 183, 79, '02 / 09 / 2005', 'Undergraduate', '6665945515', '1457599227754', '0630449029'),
    (39, 4, 'Brooke Valdez', 'C:/players/team4/Screenshot 2025-08-25 004441.png', 3, 'C:/players/team4/Screenshot 2025-08-25 004441.png', '35', 196, 62, '11 / 08 / 2005', 'Undergraduate', '6553791864', '2363469732683', '0650085325'),
    (40, 4, 'Ximena Wood', 'C:/players/team4/Screenshot 2025-08-25 004444.png', 4, 'C:/players/team4/Screenshot 2025-08-25 004444.png', '44', 185, 51, '01 / 10 / 2005', 'Undergraduate', '6620162400', '2349449673784', '0677093790'),
    (41, 4, 'Dana Rossi', 'C:/players/team4/Screenshot 2025-08-25 004448.png', 5, 'C:/players/team4/Screenshot 2025-08-25 004448.png', '54', 167, 85, '21 / 06 / 2003', 'Undergraduate', '6767822591', '1465261001514', '0975737769'),
    (42, 4, 'Paige Ibrahim', 'C:/players/team4/Screenshot 2025-08-25 004450.png', 6, 'C:/players/team4/Screenshot 2025-08-25 004450.png', '93', 186, 86, '07 / 10 / 2003', 'Undergraduate', '6504775243', '2402782545569', '0802871618'),
    (43, 4, 'Freya Ibrahim', 'C:/players/team4/Screenshot 2025-08-25 004453.png', 7, 'C:/players/team4/Screenshot 2025-08-25 004453.png', '85', 172, 80, '25 / 11 / 2003', 'Undergraduate', '6719057366', '2384821584399', '0634470565'),
    (44, 4, 'Silas Jordan', 'C:/players/team4/Screenshot 2025-08-25 004456.png', 8, 'C:/players/team4/Screenshot 2025-08-25 004456.png', '20', 200, 54, '03 / 01 / 2003', 'Undergraduate', '6729153926', '1450694925882', '0878576906'),
    (45, 4, 'Nora Wilson', 'C:/players/team4/Screenshot 2025-08-25 004459.png', 9, 'C:/players/team4/Screenshot 2025-08-25 004459.png', '05', 198, 89, '01 / 01 / 2004', 'Undergraduate', '6789841288', '2304749760939', '0989691035'),
    (46, 4, 'Theo Chung', 'C:/players/team4/Screenshot 2025-08-25 004502.png', 10, 'C:/players/team4/Screenshot 2025-08-25 004502.png', '75', 183, 81, '26 / 08 / 2005', 'Undergraduate', '6549672080', '1436582615461', '0605402926'),
    (47, 4, 'Ian Brooks', 'C:/players/team4/Screenshot 2025-08-25 004506.png', 11, 'C:/players/team4/Screenshot 2025-08-25 004506.png', '58', 194, 56, '18 / 03 / 2003', 'Undergraduate', '6551555582', '1361279435939', '0945306514'),
    (48, 4, 'Jade Young', 'C:/players/team4/Screenshot 2025-08-25 004510.png', 12, 'C:/players/team4/Screenshot 2025-08-25 004510.png', '78', 174, 57, '06 / 02 / 2004', 'Undergraduate', '6781304749', '2457398215692', '0906640454'),
    (49, 5, 'Clara Cole', 'C:/players/team5/Screenshot 2025-08-25 010501.png', 1, 'C:/players/team5/Screenshot 2025-08-25 010501.png', '69', 162, 83, '04 / 02 / 2004', 'Undergraduate', '6757742725', '1423190871145', '0912579462'),
    (50, 5, 'Tessa Clark', 'C:/players/team5/Screenshot 2025-08-25 010508.png', 2, 'C:/players/team5/Screenshot 2025-08-25 010508.png', '68', 194, 66, '16 / 06 / 2003', 'Undergraduate', '6630520984', '2442587546047', '0673110598'),
    (51, 5, 'Chase Diaz', 'C:/players/team5/Screenshot 2025-08-25 010512.png', 3, 'C:/players/team5/Screenshot 2025-08-25 010512.png', '47', 187, 96, '24 / 09 / 2005', 'Undergraduate', '6565392205', '1439230046595', '0665146377'),
    (52, 5, 'Zoe Lim', 'C:/players/team5/Screenshot 2025-08-25 010517 - Copy.png', 4, 'C:/players/team5/Screenshot 2025-08-25 010517 - Copy.png', '89', 171, 71, '20 / 05 / 2005', 'Undergraduate', '6574647250', '1451243095118', '0981103879'),
    (53, 5, 'Paige Flores', 'C:/players/team5/Screenshot 2025-08-25 010517.png', 5, 'C:/players/team5/Screenshot 2025-08-25 010517.png', '95', 165, 80, '04 / 12 / 2004', 'Undergraduate', '6605535031', '2425105535301', '0992095966'),
    (54, 5, 'Will Irwin', 'C:/players/team5/Screenshot 2025-08-25 010521.png', 6, 'C:/players/team5/Screenshot 2025-08-25 010521.png', '05', 198, 72, '08 / 01 / 2004', 'Undergraduate', '6766691822', '2376392655488', '0622461368'),
    (55, 5, 'Troy Zhang', 'C:/players/team5/Screenshot 2025-08-25 010524.png', 7, 'C:/players/team5/Screenshot 2025-08-25 010524.png', '36', 174, 98, '01 / 01 / 2003', 'Undergraduate', '6793267097', '2434083041873', '0672114771'),
    (56, 5, 'Skye Edwards', 'C:/players/team5/Screenshot 2025-08-25 010530.png', 8, 'C:/players/team5/Screenshot 2025-08-25 010530.png', '54', 159, 87, '20 / 08 / 2005', 'Undergraduate', '6777191263', '1365127534024', '0971562017'),
    (57, 5, 'Casey Ueda', 'C:/players/team5/Screenshot 2025-08-25 010532.png', 9, 'C:/players/team5/Screenshot 2025-08-25 010532.png', '39', 174, 51, '04 / 08 / 2005', 'Undergraduate', '6598609961', '1337915317763', '0888378777'),
    (58, 5, 'Logan Cooper', 'C:/players/team5/Screenshot 2025-08-25 010535.png', 10, 'C:/players/team5/Screenshot 2025-08-25 010535.png', '60', 186, 79, '09 / 07 / 2005', 'Undergraduate', '6787399740', '1452362760850', '0854540029'),
    (59, 5, 'Kara Ward', 'C:/players/team5/Screenshot 2025-08-25 010537.png', 11, 'C:/players/team5/Screenshot 2025-08-25 010537.png', '80', 179, 97, '23 / 02 / 2004', 'Undergraduate', '6568351815', '1412873722872', '0928419946'),
    (60, 5, 'Ximena Parker', 'C:/players/team5/Screenshot 2025-08-25 010540.png', 12, 'C:/players/team5/Screenshot 2025-08-25 010540.png', '79', 171, 89, '22 / 03 / 2003', 'Undergraduate', '6632823406', '1418625845805', '0631724068'),
    (61, 6, 'Alex Ortiz', 'C:/players/team6/Screenshot 2025-08-25 011707.png', 1, 'C:/players/team6/Screenshot 2025-08-25 011707.png', '50', 163, 62, '03 / 08 / 2004', 'Undergraduate', '6735087787', '1390526823050', '0865002142'),
    (62, 6, 'Blake Patel', 'C:/players/team6/Screenshot 2025-08-25 011710.png', 2, 'C:/players/team6/Screenshot 2025-08-25 011710.png', '71', 181, 50, '04 / 09 / 2005', 'Undergraduate', '6653249823', '2435900399039', '0627367918'),
    (63, 6, 'Hayden Morris', 'C:/players/team6/Screenshot 2025-08-25 011714.png', 3, 'C:/players/team6/Screenshot 2025-08-25 011714.png', '37', 183, 64, '29 / 03 / 2005', 'Undergraduate', '6634402047', '1450068965413', '0901850917'),
    (64, 6, 'Troy Hughes', 'C:/players/team6/Screenshot 2025-08-25 011717.png', 4, 'C:/players/team6/Screenshot 2025-08-25 011717.png', '87', 157, 58, '26 / 02 / 2003', 'Undergraduate', '6696496732', '1376527620981', '0962982334'),
    (65, 6, 'Reese Howard', 'C:/players/team6/Screenshot 2025-08-25 011720.png', 5, 'C:/players/team6/Screenshot 2025-08-25 011720.png', '44', 164, 71, '15 / 04 / 2003', 'Undergraduate', '6721392408', '1376571161953', '0667011340'),
    (66, 6, 'Theo Peterson', 'C:/players/team6/Screenshot 2025-08-25 011723.png', 6, 'C:/players/team6/Screenshot 2025-08-25 011723.png', '09', 169, 88, '25 / 12 / 2003', 'Undergraduate', '6569086517', '2305557521848', '0973831054'),
    (67, 6, 'Aria Foster', 'C:/players/team6/Screenshot 2025-08-25 011725.png', 7, 'C:/players/team6/Screenshot 2025-08-25 011725.png', '34', 167, 97, '19 / 02 / 2004', 'Undergraduate', '6699327980', '1329430655138', '0805310047'),
    (68, 6, 'Gavin Lam', 'C:/players/team6/Screenshot 2025-08-25 011729.png', 8, 'C:/players/team6/Screenshot 2025-08-25 011729.png', '56', 160, 69, '12 / 09 / 2003', 'Undergraduate', '6686585119', '2395721411094', '0618285901'),
    (69, 6, 'Wade Holland', 'C:/players/team6/Screenshot 2025-08-25 011732.png', 9, 'C:/players/team6/Screenshot 2025-08-25 011732.png', '40', 192, 51, '02 / 06 / 2003', 'Undergraduate', '6543355445', '2409267939354', '0622449153'),
    (70, 6, 'Ronan Bishop', 'C:/players/team6/Screenshot 2025-08-25 011735.png', 10, 'C:/players/team6/Screenshot 2025-08-25 011735.png', '32', 172, 60, '09 / 05 / 2003', 'Undergraduate', '6560557226', '2335364455517', '0861466935'),
    (71, 6, 'Dominic Vargas', 'C:/players/team6/Screenshot 2025-08-25 011737.png', 11, 'C:/players/team6/Screenshot 2025-08-25 011737.png', '55', 156, 59, '24 / 10 / 2005', 'Undergraduate', '6517554252', '1480686347549', '0843040968'),
    (72, 6, 'Troy Walsh', 'C:/players/team6/Screenshot 2025-08-25 011740.png', 12, 'C:/players/team6/Screenshot 2025-08-25 011740.png', '41', 165, 53, '12 / 06 / 2005', 'Undergraduate', '6704781384', '1302552798697', '0886695488'),
    (73, 7, 'Wren Barnes', 'C:/players/team7/Screenshot 2025-08-25 011945.png', 1, 'C:/players/team7/Screenshot 2025-08-25 011945.png', '26', 176, 75, '13 / 07 / 2004', 'Undergraduate', '6705108191', '2395060811542', '0652457056'),
    (74, 7, 'June Simmons', 'C:/players/team7/Screenshot 2025-08-25 011947.png', 2, 'C:/players/team7/Screenshot 2025-08-25 011947.png', '36', 160, 93, '03 / 10 / 2004', 'Undergraduate', '6672295301', '1443925900645', '0803502507'),
    (75, 7, 'Wren Barker', 'C:/players/team7/Screenshot 2025-08-25 011950.png', 3, 'C:/players/team7/Screenshot 2025-08-25 011950.png', '58', 190, 96, '27 / 09 / 2004', 'Undergraduate', '6629230630', '2301121440308', '0829903283'),
    (76, 7, 'Logan Coleman', 'C:/players/team7/Screenshot 2025-08-25 011953.png', 4, 'C:/players/team7/Screenshot 2025-08-25 011953.png', '91', 169, 82, '20 / 01 / 2005', 'Undergraduate', '6639379684', '2452228171177', '0672770008'),
    (77, 7, 'Clara Xu', 'C:/players/team7/Screenshot 2025-08-25 011956.png', 5, 'C:/players/team7/Screenshot 2025-08-25 011956.png', '43', 156, 58, '18 / 05 / 2005', 'Undergraduate', '6668977937', '1469148100816', '0814117254'),
    (78, 7, 'Finn Diaz', 'C:/players/team7/Screenshot 2025-08-25 011958.png', 6, 'C:/players/team7/Screenshot 2025-08-25 011958.png', '93', 190, 80, '21 / 11 / 2005', 'Undergraduate', '6518313575', '1352211994399', '0816483752'),
    (79, 7, 'Parker Wood', 'C:/players/team7/Screenshot 2025-08-25 012001.png', 7, 'C:/players/team7/Screenshot 2025-08-25 012001.png', '19', 168, 61, '26 / 01 / 2004', 'Undergraduate', '6612443584', '1385007188161', '0931364705'),
    (80, 7, 'Bella Nguyen', 'C:/players/team7/Screenshot 2025-08-25 012003.png', 8, 'C:/players/team7/Screenshot 2025-08-25 012003.png', '76', 166, 66, '21 / 07 / 2005', 'Undergraduate', '6799348684', '1449123801306', '0628648891'),
    (81, 7, 'Clara Lane', 'C:/players/team7/Screenshot 2025-08-25 012006.png', 9, 'C:/players/team7/Screenshot 2025-08-25 012006.png', '73', 184, 71, '24 / 02 / 2005', 'Undergraduate', '6794091089', '1338063537357', '0864309850'),
    (82, 7, 'Kara Nguyen', 'C:/players/team7/Screenshot 2025-08-25 012008.png', 10, 'C:/players/team7/Screenshot 2025-08-25 012008.png', '95', 192, 87, '18 / 09 / 2005', 'Undergraduate', '6620148029', '2452907735775', '0992070521'),
    (83, 7, 'Lola Powell', 'C:/players/team7/Screenshot 2025-08-25 012010.png', 11, 'C:/players/team7/Screenshot 2025-08-25 012010.png', '16', 199, 68, '25 / 10 / 2003', 'Undergraduate', '6591085329', '2470237671797', '0847053818'),
    (84, 7, 'Eli Ueda', 'C:/players/team7/Screenshot 2025-08-25 012013.png', 12, 'C:/players/team7/Screenshot 2025-08-25 012013.png', '44', 159, 64, '27 / 12 / 2005', 'Undergraduate', '6793118954', '2499000582159', '0662245899'),
    (85, 8, 'Georgia Ibrahim', 'C:/players/team8/Screenshot 2025-08-25 012335.png', 1, 'C:/players/team8/Screenshot 2025-08-25 012335.png', '55', 185, 70, '19 / 03 / 2005', 'Undergraduate', '6510532783', '1482241192052', '0809154538'),
    (86, 8, 'Lola Ueda', 'C:/players/team8/Screenshot 2025-08-25 012337.png', 2, 'C:/players/team8/Screenshot 2025-08-25 012337.png', '83', 179, 73, '29 / 07 / 2005', 'Undergraduate', '6511546618', '1366680136496', '0649794213'),
    (87, 8, 'Sage Henderson', 'C:/players/team8/Screenshot 2025-08-25 012340.png', 3, 'C:/players/team8/Screenshot 2025-08-25 012340.png', '40', 178, 86, '16 / 09 / 2003', 'Undergraduate', '6799593865', '1387043216911', '0875868024'),
    (88, 8, 'Evan Barker', 'C:/players/team8/Screenshot 2025-08-25 012344.png', 4, 'C:/players/team8/Screenshot 2025-08-25 012344.png', '20', 163, 64, '26 / 08 / 2003', 'Undergraduate', '6597567243', '1484171614591', '0614722605'),
    (89, 8, 'Opal Clark', 'C:/players/team8/Screenshot 2025-08-25 012348.png', 5, 'C:/players/team8/Screenshot 2025-08-25 012348.png', '08', 192, 92, '03 / 04 / 2003', 'Undergraduate', '6665441386', '1393295308352', '0943400037'),
    (90, 8, 'Finn Lim', 'C:/players/team8/Screenshot 2025-08-25 012351.png', 6, 'C:/players/team8/Screenshot 2025-08-25 012351.png', '63', 167, 59, '20 / 08 / 2003', 'Undergraduate', '6760815434', '1387716642583', '0947060625'),
    (91, 8, 'Skye Chung', 'C:/players/team8/Screenshot 2025-08-25 012354.png', 7, 'C:/players/team8/Screenshot 2025-08-25 012354.png', '36', 199, 91, '23 / 07 / 2005', 'Undergraduate', '6718910183', '1459487749149', '0681030173'),
    (92, 8, 'Colin Rogers', 'C:/players/team8/Screenshot 2025-08-25 012359.png', 8, 'C:/players/team8/Screenshot 2025-08-25 012359.png', '15', 197, 54, '03 / 09 / 2003', 'Undergraduate', '6593036889', '1434054375477', '0926380304'),
    (93, 8, 'Mila Peterson', 'C:/players/team8/Screenshot 2025-08-25 012402.png', 9, 'C:/players/team8/Screenshot 2025-08-25 012402.png', '72', 187, 72, '07 / 02 / 2003', 'Undergraduate', '6571908785', '1391444086311', '0930837317'),
    (94, 8, 'Nora Ibrahim', 'C:/players/team8/Screenshot 2025-08-25 012407.png', 10, 'C:/players/team8/Screenshot 2025-08-25 012407.png', '57', 187, 53, '10 / 10 / 2003', 'Undergraduate', '6784761674', '2395272113253', '0889818996'),
    (95, 8, 'Parker Anderson', 'C:/players/team8/Screenshot 2025-08-25 012410.png', 11, 'C:/players/team8/Screenshot 2025-08-25 012410.png', '90', 189, 53, '05 / 10 / 2005', 'Undergraduate', '6765645053', '2477721715884', '0973624131'),
    (96, 8, 'Aria Barker', 'C:/players/team8/Screenshot 2025-08-25 012414.png', 12, 'C:/players/team8/Screenshot 2025-08-25 012414.png', '45', 183, 78, '02 / 02 / 2003', 'Undergraduate', '6513092652', '2400277729729', '0811893294'),
    (97, 9, 'Felix Bailey', 'C:/players/team9/Screenshot 2025-08-25 012920.png', 1, 'C:/players/team9/Screenshot 2025-08-25 012920.png', '74', 156, 72, '18 / 12 / 2004', 'Undergraduate', '6513942789', '1424561056046', '0854144184'),
    (98, 9, 'Adrian Edwards', 'C:/players/team9/Screenshot 2025-08-25 012923.png', 2, 'C:/players/team9/Screenshot 2025-08-25 012923.png', '69', 157, 94, '16 / 04 / 2005', 'Undergraduate', '6616501610', '2368183027516', '0876872555'),
    (99, 9, 'Georgia Henderson', 'C:/players/team9/Screenshot 2025-08-25 012926.png', 3, 'C:/players/team9/Screenshot 2025-08-25 012926.png', '68', 179, 82, '08 / 09 / 2004', 'Undergraduate', '6646080873', '2369069546357', '0602501803'),
    (100, 9, 'Naomi Rogers', 'C:/players/team9/Screenshot 2025-08-25 012928.png', 4, 'C:/players/team9/Screenshot 2025-08-25 012928.png', '46', 187, 74, '18 / 05 / 2004', 'Undergraduate', '6614056336', '2460108631454', '0677860523'),
    (101, 9, 'Hayden Turner', 'C:/players/team9/Screenshot 2025-08-25 012931.png', 5, 'C:/players/team9/Screenshot 2025-08-25 012931.png', '73', 178, 85, '15 / 05 / 2003', 'Undergraduate', '6688538100', '2411341890069', '0648539509'),
    (102, 9, 'Olivia Valdez', 'C:/players/team9/Screenshot 2025-08-25 012933.png', 6, 'C:/players/team9/Screenshot 2025-08-25 012933.png', '48', 168, 87, '26 / 09 / 2003', 'Undergraduate', '6501844902', '1494721316342', '0638856560'),
    (103, 9, 'Will Patel', 'C:/players/team9/Screenshot 2025-08-25 012936.png', 7, 'C:/players/team9/Screenshot 2025-08-25 012936.png', '72', 156, 67, '23 / 03 / 2004', 'Undergraduate', '6749499460', '2340714544497', '0967453040'),
    (104, 9, 'Iris Lane', 'C:/players/team9/Screenshot 2025-08-25 012940.png', 8, 'C:/players/team9/Screenshot 2025-08-25 012940.png', '39', 197, 93, '18 / 09 / 2004', 'Undergraduate', '6577606999', '1341593746666', '0865326167'),
    (105, 9, 'Will Nolan', 'C:/players/team9/Screenshot 2025-08-25 012944.png', 9, 'C:/players/team9/Screenshot 2025-08-25 012944.png', '32', 186, 95, '12 / 12 / 2004', 'Undergraduate', '6563220982', '2371582509283', '0921527401'),
    (106, 9, 'Brandon Fuller', 'C:/players/team9/Screenshot 2025-08-25 012948.png', 10, 'C:/players/team9/Screenshot 2025-08-25 012948.png', '34', 191, 96, '24 / 03 / 2004', 'Undergraduate', '6566992918', '2426122869832', '0617845284'),
    (107, 9, 'Ian Taylor', 'C:/players/team9/Screenshot 2025-08-25 012952.png', 11, 'C:/players/team9/Screenshot 2025-08-25 012952.png', '23', 191, 65, '10 / 04 / 2003', 'Undergraduate', '6764449855', '1354481197418', '0665959788'),
    (108, 9, 'Blake Kim', 'C:/players/team9/Screenshot 2025-08-25 012956.png', 12, 'C:/players/team9/Screenshot 2025-08-25 012956.png', '89', 195, 80, '16 / 09 / 2004', 'Undergraduate', '6505791923', '2322906609769', '0996674468'),
    (109, 10, 'Hazel Lopez', 'C:/players/team10/Screenshot 2025-08-25 013558.png', 1, 'C:/players/team10/Screenshot 2025-08-25 013558.png', '77', 169, 80, '08 / 10 / 2003', 'Undergraduate', '6792724679', '2425420341339', '0893980206'),
    (110, 10, 'Parker Yates', 'C:/players/team10/Screenshot 2025-08-25 013603.png', 2, 'C:/players/team10/Screenshot 2025-08-25 013603.png', '71', 196, 85, '10 / 05 / 2003', 'Undergraduate', '6512864725', '2467528412697', '0985982465'),
    (111, 10, 'Georgia Wood', 'C:/players/team10/Screenshot 2025-08-25 013608.png', 3, 'C:/players/team10/Screenshot 2025-08-25 013608.png', '94', 182, 61, '13 / 08 / 2005', 'Undergraduate', '6797276653', '2490364363323', '0858237660'),
    (112, 10, 'Nora Clark', 'C:/players/team10/Screenshot 2025-08-25 013611.png', 4, 'C:/players/team10/Screenshot 2025-08-25 013611.png', '99', 179, 50, '29 / 07 / 2003', 'Undergraduate', '6669397933', '1373859857644', '0674193047'),
    (113, 10, 'Skye Taylor', 'C:/players/team10/Screenshot 2025-08-25 013615.png', 5, 'C:/players/team10/Screenshot 2025-08-25 013615.png', '63', 170, 71, '22 / 10 / 2005', 'Undergraduate', '6716066340', '2409870540875', '0670642582'),
    (114, 10, 'Dylan Barker', 'C:/players/team10/Screenshot 2025-08-25 013618.png', 6, 'C:/players/team10/Screenshot 2025-08-25 013618.png', '67', 193, 74, '12 / 02 / 2004', 'Undergraduate', '6556450246', '2474167414123', '0859161187'),
    (115, 10, 'Colin Mehta', 'C:/players/team10/Screenshot 2025-08-25 013621.png', 7, 'C:/players/team10/Screenshot 2025-08-25 013621.png', '97', 186, 52, '07 / 12 / 2003', 'Undergraduate', '6588582000', '1343470851706', '0959360801'),
    (116, 10, 'Noah Quinn', 'C:/players/team10/Screenshot 2025-08-25 013624.png', 8, 'C:/players/team10/Screenshot 2025-08-25 013624.png', '91', 184, 60, '06 / 08 / 2004', 'Undergraduate', '6549895369', '2349299347526', '0620216831'),
    (117, 10, 'Keira Lam', 'C:/players/team10/Screenshot 2025-08-25 013628.png', 9, 'C:/players/team10/Screenshot 2025-08-25 013628.png', '65', 171, 80, '10 / 07 / 2004', 'Undergraduate', '6655075585', '2478512638969', '0856217672'),
    (118, 10, 'Faith Schmidt', 'C:/players/team10/Screenshot 2025-08-25 013631.png', 10, 'C:/players/team10/Screenshot 2025-08-25 013631.png', '50', 164, 66, '02 / 08 / 2005', 'Undergraduate', '6551369509', '1455977099392', '0617294867'),
    (119, 10, 'Liam Perry', 'C:/players/team10/Screenshot 2025-08-25 013633.png', 11, 'C:/players/team10/Screenshot 2025-08-25 013633.png', '58', 155, 96, '02 / 03 / 2004', 'Undergraduate', '6622965993', '2402929897719', '0931921508'),
    (120, 10, 'Iris Davis', 'C:/players/team10/Screenshot 2025-08-25 013636.png', 12, 'C:/players/team10/Screenshot 2025-08-25 013636.png', '13', 182, 64, '09 / 09 / 2004', 'Undergraduate', '6726280917', '1396686262914', '0688367353'),
    (121, 11, 'Ivy Khan', 'C:/players/team11/Screenshot 2025-08-25 014216.png', 1, 'C:/players/team11/Screenshot 2025-08-25 014216.png', '22', 191, 65, '06 / 03 / 2004', 'Undergraduate', '6575720687', '2345567244553', '0970450121'),
    (122, 11, 'Hunter Xu', 'C:/players/team11/Screenshot 2025-08-25 014219.png', 2, 'C:/players/team11/Screenshot 2025-08-25 014219.png', '18', 173, 57, '29 / 12 / 2004', 'Undergraduate', '6762674595', '2470967784398', '0997631250'),
    (123, 11, 'Dana Lim', 'C:/players/team11/Screenshot 2025-08-25 014223.png', 3, 'C:/players/team11/Screenshot 2025-08-25 014223.png', '20', 185, 78, '26 / 11 / 2003', 'Undergraduate', '6753832368', '2348899753729', '0694204106'),
    (124, 11, 'Vera Price', 'C:/players/team11/Screenshot 2025-08-25 014225.png', 4, 'C:/players/team11/Screenshot 2025-08-25 014225.png', '78', 165, 57, '03 / 09 / 2005', 'Undergraduate', '6704097549', '2437521932725', '0605620575'),
    (125, 11, 'Paige Johns', 'C:/players/team11/Screenshot 2025-08-25 014230.png', 5, 'C:/players/team11/Screenshot 2025-08-25 014230.png', '97', 185, 90, '04 / 02 / 2005', 'Undergraduate', '6506507862', '2331052414081', '0820983633'),
    (126, 11, 'Naomi Zhou', 'C:/players/team11/Screenshot 2025-08-25 014235.png', 6, 'C:/players/team11/Screenshot 2025-08-25 014235.png', '32', 186, 94, '10 / 10 / 2004', 'Undergraduate', '6507412689', '1411339196985', '0819695616'),
    (127, 11, 'Brandon Patterson', 'C:/players/team11/Screenshot 2025-08-25 014239.png', 7, 'C:/players/team11/Screenshot 2025-08-25 014239.png', '56', 180, 62, '17 / 08 / 2004', 'Undergraduate', '6530293297', '2432393644132', '0838188598'),
    (128, 11, 'Quinn Bishop', 'C:/players/team11/Screenshot 2025-08-25 014242.png', 8, 'C:/players/team11/Screenshot 2025-08-25 014242.png', '60', 178, 70, '31 / 12 / 2003', 'Undergraduate', '6687292300', '1482432435570', '0648958903'),
    (129, 11, 'Silas Takagi', 'C:/players/team11/Screenshot 2025-08-25 014245.png', 9, 'C:/players/team11/Screenshot 2025-08-25 014245.png', '02', 193, 63, '05 / 08 / 2005', 'Undergraduate', '6703141318', '1357284653073', '0844684484'),
    (130, 11, 'Skye Usman', 'C:/players/team11/Screenshot 2025-08-25 014248.png', 10, 'C:/players/team11/Screenshot 2025-08-25 014248.png', '85', 200, 81, '13 / 11 / 2004', 'Undergraduate', '6740807838', '1303620639511', '0673446559'),
    (131, 11, 'Miles Bailey', 'C:/players/team11/Screenshot 2025-08-25 014250.png', 11, 'C:/players/team11/Screenshot 2025-08-25 014250.png', '28', 195, 92, '27 / 01 / 2004', 'Undergraduate', '6560939873', '1346353107752', '0687312576'),
    (132, 11, 'Uma Ibrahim', 'C:/players/team11/Screenshot 2025-08-25 014253.png', 12, 'C:/players/team11/Screenshot 2025-08-25 014253.png', '10', 180, 56, '04 / 03 / 2004', 'Undergraduate', '6668315279', '2414631926352', '0839924690'),
    (133, 12, 'Zayne Johns', 'C:/players/team12/Screenshot 2025-08-25 015011.png', 1, 'C:/players/team12/Screenshot 2025-08-25 015011.png', '52', 200, 78, '25 / 07 / 2004', 'Undergraduate', '6551097273', '2410397013763', '0690572288'),
    (134, 12, 'Naomi Peterson', 'C:/players/team12/Screenshot 2025-08-25 015014.png', 2, 'C:/players/team12/Screenshot 2025-08-25 015014.png', '04', 169, 93, '21 / 11 / 2004', 'Undergraduate', '6561191058', '1329666286756', '0946635612'),
    (135, 12, 'Reed Flores', 'C:/players/team12/Screenshot 2025-08-25 015017.png', 3, 'C:/players/team12/Screenshot 2025-08-25 015017.png', '97', 182, 71, '11 / 07 / 2004', 'Undergraduate', '6644868830', '1433585742658', '0980884086'),
    (136, 12, 'Paige Cooper', 'C:/players/team12/Screenshot 2025-08-25 015020.png', 4, 'C:/players/team12/Screenshot 2025-08-25 015020.png', '09', 173, 85, '23 / 08 / 2004', 'Undergraduate', '6797812626', '1382414166938', '0921402571'),
    (137, 12, 'Yosef Underwood', 'C:/players/team12/Screenshot 2025-08-25 015024.png', 5, 'C:/players/team12/Screenshot 2025-08-25 015024.png', '53', 179, 73, '10 / 08 / 2005', 'Undergraduate', '6565603165', '1362994550062', '0618144467'),
    (138, 12, 'Ivy Zimmerman', 'C:/players/team12/Screenshot 2025-08-25 015027.png', 6, 'C:/players/team12/Screenshot 2025-08-25 015027.png', '86', 158, 72, '11 / 04 / 2004', 'Undergraduate', '6772483328', '1357694543219', '0868660429'),
    (139, 12, 'Nash Ramirez', 'C:/players/team12/Screenshot 2025-08-25 015030.png', 7, 'C:/players/team12/Screenshot 2025-08-25 015030.png', '69', 163, 78, '28 / 06 / 2003', 'Undergraduate', '6651467196', '1432700809364', '0628106458'),
    (140, 12, 'Elias D''''Angelo', 'C:/players/team12/Screenshot 2025-08-25 015035.png', 8, 'C:/players/team12/Screenshot 2025-08-25 015035.png', '70', 188, 85, '03 / 02 / 2004', 'Undergraduate', '6679901440', '2350650776422', '0657818814'),
    (141, 12, 'Nash Smith', 'C:/players/team12/Screenshot 2025-08-25 015038.png', 9, 'C:/players/team12/Screenshot 2025-08-25 015038.png', '03', 157, 71, '20 / 04 / 2004', 'Undergraduate', '6729878306', '2432221746999', '0847209082'),
    (142, 12, 'Dominic Hughes', 'C:/players/team12/Screenshot 2025-08-25 015044.png', 10, 'C:/players/team12/Screenshot 2025-08-25 015044.png', '76', 177, 78, '12 / 03 / 2004', 'Undergraduate', '6537572303', '2379934709477', '0664110170'),
    (143, 12, 'Elias Wilson', 'C:/players/team12/Screenshot 2025-08-25 015048.png', 11, 'C:/players/team12/Screenshot 2025-08-25 015048.png', '77', 158, 93, '26 / 12 / 2004', 'Undergraduate', '6704739758', '2423943445774', '0972092306'),
    (144, 12, 'Riley Reed', 'C:/players/team12/Screenshot 2025-08-25 015052.png', 12, 'C:/players/team12/Screenshot 2025-08-25 015052.png', '11', 163, 66, '22 / 09 / 2005', 'Undergraduate', '6683457360', '1350991275981', '0849005952'),
    (145, 13, 'Owen Vega', 'C:/players/team13/Screenshot 2025-08-25 021127.png', 1, 'C:/players/team13/Screenshot 2025-08-25 021127.png', '45', 179, 92, '09 / 04 / 2003', 'Undergraduate', '6712943768', '2417797064744', '0848225578'),
    (146, 13, 'Kylie Underwood', 'C:/players/team13/Screenshot 2025-08-25 021129.png', 2, 'C:/players/team13/Screenshot 2025-08-25 021129.png', '69', 164, 69, '06 / 02 / 2003', 'Undergraduate', '6576735889', '2488147898161', '0855651375'),
    (147, 13, 'Kylie Irwin', 'C:/players/team13/Screenshot 2025-08-25 021132.png', 3, 'C:/players/team13/Screenshot 2025-08-25 021132.png', '79', 189, 54, '01 / 07 / 2003', 'Undergraduate', '6613120937', '2422039671687', '0647459001'),
    (148, 13, 'Finn Ng', 'C:/players/team13/Screenshot 2025-08-25 021134.png', 4, 'C:/players/team13/Screenshot 2025-08-25 021134.png', '48', 159, 82, '14 / 08 / 2004', 'Undergraduate', '6626978456', '2367252357019', '0920618201'),
    (149, 13, 'Noah Rowe', 'C:/players/team13/Screenshot 2025-08-25 021138.png', 5, 'C:/players/team13/Screenshot 2025-08-25 021138.png', '35', 199, 89, '25 / 02 / 2004', 'Undergraduate', '6595236168', '2468968543251', '0699746393'),
    (150, 13, 'Miles Murphy', 'C:/players/team13/Screenshot 2025-08-25 021141.png', 6, 'C:/players/team13/Screenshot 2025-08-25 021141.png', '71', 161, 62, '24 / 05 / 2004', 'Undergraduate', '6520381642', '2487534025896', '0943093774'),
    (151, 13, 'Lola Irwin', 'C:/players/team13/Screenshot 2025-08-25 021144.png', 7, 'C:/players/team13/Screenshot 2025-08-25 021144.png', '77', 162, 92, '20 / 09 / 2003', 'Undergraduate', '6689685412', '1431348303888', '0873843327'),
    (152, 13, 'Adrian Patterson', 'C:/players/team13/Screenshot 2025-08-25 021151.png', 8, 'C:/players/team13/Screenshot 2025-08-25 021151.png', '30', 178, 77, '04 / 08 / 2004', 'Undergraduate', '6657793645', '1364558536581', '0979150307'),
    (153, 13, 'Kai Rogers', 'C:/players/team13/Screenshot 2025-08-25 021154.png', 9, 'C:/players/team13/Screenshot 2025-08-25 021154.png', '90', 186, 51, '04 / 04 / 2004', 'Undergraduate', '6551990832', '1382605735376', '0629680287'),
    (154, 13, 'Jade Vargas', 'C:/players/team13/Screenshot 2025-08-25 021158.png', 10, 'C:/players/team13/Screenshot 2025-08-25 021158.png', '64', 174, 77, '28 / 03 / 2005', 'Undergraduate', '6645723657', '1443540751101', '0908874976'),
    (155, 13, 'Noah Davis', 'C:/players/team13/Screenshot 2025-08-25 021200.png', 11, 'C:/players/team13/Screenshot 2025-08-25 021200.png', '51', 178, 66, '01 / 09 / 2004', 'Undergraduate', '6739988497', '2425795638229', '0627579454'),
    (156, 13, 'Ximena Kelly', 'C:/players/team13/Screenshot 2025-08-25 021203.png', 12, 'C:/players/team13/Screenshot 2025-08-25 021203.png', '67', 163, 84, '13 / 12 / 2004', 'Undergraduate', '6660158056', '1335990960587', '0841599886'),
    (157, 14, 'Jade Anderson', 'C:/players/team14/Screenshot 2025-08-25 024511.png', 1, 'C:/players/team14/Screenshot 2025-08-25 024511.png', '08', 199, 85, '19 / 12 / 2003', 'Undergraduate', '6678564791', '1452757283833', '0994196804'),
    (158, 14, 'Omar Valdez', 'C:/players/team14/Screenshot 2025-08-25 024514.png', 2, 'C:/players/team14/Screenshot 2025-08-25 024514.png', '12', 171, 65, '25 / 10 / 2005', 'Undergraduate', '6671363157', '2490594710611', '0622684483'),
    (159, 14, 'Piper Ortiz', 'C:/players/team14/Screenshot 2025-08-25 024516.png', 3, 'C:/players/team14/Screenshot 2025-08-25 024516.png', '45', 164, 85, '04 / 03 / 2005', 'Undergraduate', '6738809931', '2443656667473', '0935877232'),
    (160, 14, 'Kara Usman', 'C:/players/team14/Screenshot 2025-08-25 024519.png', 4, 'C:/players/team14/Screenshot 2025-08-25 024519.png', '72', 171, 50, '08 / 05 / 2004', 'Undergraduate', '6796208531', '2489116653915', '0969668737'),
    (161, 14, 'Avery Vargas', 'C:/players/team14/Screenshot 2025-08-25 024522.png', 5, 'C:/players/team14/Screenshot 2025-08-25 024522.png', '71', 187, 95, '03 / 05 / 2005', 'Undergraduate', '6542194660', '2336306542519', '0853206778'),
    (162, 14, 'Liam Taylor', 'C:/players/team14/Screenshot 2025-08-25 024526.png', 6, 'C:/players/team14/Screenshot 2025-08-25 024526.png', '27', 178, 85, '03 / 02 / 2003', 'Undergraduate', '6559735315', '2308701184974', '0927271411'),
    (163, 14, 'Quinn Yates', 'C:/players/team14/Screenshot 2025-08-25 024529.png', 7, 'C:/players/team14/Screenshot 2025-08-25 024529.png', '87', 180, 69, '23 / 01 / 2005', 'Undergraduate', '6509036068', '2378683436571', '0965245566'),
    (164, 14, 'Ivy Henderson', 'C:/players/team14/Screenshot 2025-08-25 024531.png', 8, 'C:/players/team14/Screenshot 2025-08-25 024531.png', '54', 155, 67, '01 / 04 / 2005', 'Undergraduate', '6644846257', '1414038267801', '0975203301'),
    (165, 14, 'Silas Turner', 'C:/players/team14/Screenshot 2025-08-25 024536.png', 9, 'C:/players/team14/Screenshot 2025-08-25 024536.png', '47', 183, 98, '21 / 08 / 2005', 'Undergraduate', '6780293952', '2492041466327', '0605524987'),
    (166, 14, 'Keira Morgan', 'C:/players/team14/Screenshot 2025-08-25 025034.png', 10, 'C:/players/team14/Screenshot 2025-08-25 025034.png', '40', 174, 63, '05 / 04 / 2004', 'Undergraduate', '6789228702', '1474813086483', '0632980077'),
    (167, 14, 'Olivia Larson', 'C:/players/team14/Screenshot 2025-08-25 025037.png', 11, 'C:/players/team14/Screenshot 2025-08-25 025037.png', '74', 199, 64, '18 / 08 / 2004', 'Undergraduate', '6542165914', '1441276571491', '0917004075'),
    (168, 14, 'Wade Shaw', 'C:/players/team14/Screenshot 2025-08-25 025041.png', 12, 'C:/players/team14/Screenshot 2025-08-25 025041.png', '03', 168, 84, '23 / 05 / 2003', 'Undergraduate', '6709826280', '2425928499101', '0976600123'),
    (169, 15, 'Mason Hall', 'C:/players/team15/Screenshot 2025-09-08 030239.png', 1, 'C:/players/team15/Screenshot 2025-09-08 030239.png', '33', 183, 74, '19 / 09 / 2005', 'Undergraduate', '6509679973', '2369223176216', '0639829053'),
    (170, 15, 'Jay Takagi', 'C:/players/team15/Screenshot 2025-09-08 030241.png', 2, 'C:/players/team15/Screenshot 2025-09-08 030241.png', '80', 166, 83, '07 / 09 / 2004', 'Undergraduate', '6677381328', '2307457722754', '0818162764'),
    (171, 15, 'Parker Murphy', 'C:/players/team15/Screenshot 2025-09-08 030244.png', 3, 'C:/players/team15/Screenshot 2025-09-08 030244.png', '26', 167, 52, '23 / 02 / 2003', 'Undergraduate', '6704208471', '1387493539532', '0868590497'),
    (172, 15, 'Freya Price', 'C:/players/team15/Screenshot 2025-09-08 030247.png', 4, 'C:/players/team15/Screenshot 2025-09-08 030247.png', '28', 176, 82, '11 / 11 / 2005', 'Undergraduate', '6518299269', '2455877482885', '0648313857'),
    (173, 15, 'Yara Schmidt', 'C:/players/team15/Screenshot 2025-09-08 030250.png', 5, 'C:/players/team15/Screenshot 2025-09-08 030250.png', '66', 192, 74, '30 / 09 / 2005', 'Undergraduate', '6654956618', '2428749524472', '0943380628'),
    (174, 15, 'Kylie Rivera', 'C:/players/team15/Screenshot 2025-09-08 030253.png', 6, 'C:/players/team15/Screenshot 2025-09-08 030253.png', '23', 200, 62, '07 / 06 / 2005', 'Undergraduate', '6620481309', '2433006688727', '0625854380'),
    (175, 15, 'Paige Zhou', 'C:/players/team15/Screenshot 2025-09-08 030256.png', 7, 'C:/players/team15/Screenshot 2025-09-08 030256.png', '73', 198, 93, '28 / 04 / 2004', 'Undergraduate', '6578738625', '1437481021109', '0604781150'),
    (176, 15, 'Quincy Ibrahim', 'C:/players/team15/Screenshot 2025-09-08 030259.png', 8, 'C:/players/team15/Screenshot 2025-09-08 030259.png', '47', 157, 89, '02 / 10 / 2003', 'Undergraduate', '6613616956', '1407555710182', '0894793132'),
    (177, 15, 'Tessa Lane', 'C:/players/team15/Screenshot 2025-09-08 030302.png', 9, 'C:/players/team15/Screenshot 2025-09-08 030302.png', '52', 182, 84, '17 / 12 / 2003', 'Undergraduate', '6684630680', '1419437358286', '0965494514'),
    (178, 15, 'Jade Morgan', 'C:/players/team15/Screenshot 2025-09-08 030305.png', 10, 'C:/players/team15/Screenshot 2025-09-08 030305.png', '51', 160, 58, '04 / 11 / 2003', 'Undergraduate', '6722106408', '2478412304481', '0830470333'),
    (179, 15, 'Ronan Flores', 'C:/players/team15/Screenshot 2025-09-08 030312.png', 11, 'C:/players/team15/Screenshot 2025-09-08 030312.png', '06', 190, 84, '03 / 06 / 2005', 'Undergraduate', '6651663637', '1497614152560', '0610112740'),
    (180, 15, 'Dylan Perry', 'C:/players/team15/Screenshot 2025-09-08 030314.png', 12, 'C:/players/team15/Screenshot 2025-09-08 030314.png', '84', 155, 68, '03 / 07 / 2004', 'Undergraduate', '6622330586', '2491756894208', '0949153753'),
    (181, 16, 'Zoe Holland', 'C:/players/team16/Screenshot 2025-09-08 030343.png', 1, 'C:/players/team16/Screenshot 2025-09-08 030343.png', '65', 192, 76, '13 / 03 / 2005', 'Undergraduate', '6674415702', '1434801408073', '0602153543'),
    (182, 16, 'Dylan Jones', 'C:/players/team16/Screenshot 2025-09-08 030345.png', 2, 'C:/players/team16/Screenshot 2025-09-08 030345.png', '60', 179, 85, '20 / 09 / 2004', 'Undergraduate', '6650714291', '1417790687985', '0694138116'),
    (183, 16, 'Olivia Mitchell', 'C:/players/team16/Screenshot 2025-09-08 030349.png', 3, 'C:/players/team16/Screenshot 2025-09-08 030349.png', '36', 168, 98, '21 / 10 / 2003', 'Undergraduate', '6744190707', '2409076979076', '0973936280'),
    (184, 16, 'Ronan Peterson', 'C:/players/team16/Screenshot 2025-09-08 030352.png', 4, 'C:/players/team16/Screenshot 2025-09-08 030352.png', '55', 162, 97, '03 / 08 / 2003', 'Undergraduate', '6672545033', '1474959881288', '0948805270'),
    (185, 16, 'Blake Bailey', 'C:/players/team16/Screenshot 2025-09-08 030355.png', 5, 'C:/players/team16/Screenshot 2025-09-08 030355.png', '04', 165, 94, '07 / 03 / 2004', 'Undergraduate', '6693510509', '2448385039620', '0634787117'),
    (186, 16, 'Jasper Howard', 'C:/players/team16/Screenshot 2025-09-08 030357.png', 6, 'C:/players/team16/Screenshot 2025-09-08 030357.png', '69', 167, 63, '23 / 05 / 2005', 'Undergraduate', '6773804854', '2434161639697', '0961683982'),
    (187, 16, 'Sienna Shaw', 'C:/players/team16/Screenshot 2025-09-08 030400.png', 7, 'C:/players/team16/Screenshot 2025-09-08 030400.png', '11', 176, 56, '28 / 11 / 2003', 'Undergraduate', '6582697699', '1443335254567', '0947972149'),
    (188, 16, 'Blake Carter', 'C:/players/team16/Screenshot 2025-09-08 030403.png', 8, 'C:/players/team16/Screenshot 2025-09-08 030403.png', '87', 168, 86, '03 / 12 / 2003', 'Undergraduate', '6615037404', '1392022022837', '0979807767'),
    (189, 16, 'Isaac Schmidt', 'C:/players/team16/Screenshot 2025-09-08 030405.png', 9, 'C:/players/team16/Screenshot 2025-09-08 030405.png', '17', 158, 86, '06 / 08 / 2005', 'Undergraduate', '6740153442', '2428407693599', '0664259082'),
    (190, 16, 'Logan Ueda', 'C:/players/team16/Screenshot 2025-09-08 030408.png', 10, 'C:/players/team16/Screenshot 2025-09-08 030408.png', '08', 157, 57, '30 / 03 / 2004', 'Undergraduate', '6590952379', '2354170277841', '0987795439'),
    (191, 16, 'Avery Tan', 'C:/players/team16/Screenshot 2025-09-08 030411.png', 11, 'C:/players/team16/Screenshot 2025-09-08 030411.png', '97', 159, 87, '11 / 11 / 2004', 'Undergraduate', '6630818392', '1302690741879', '0961934833'),
    (192, 16, 'Violet Fuller', 'C:/players/team16/Screenshot 2025-09-08 030415.png', 12, 'C:/players/team16/Screenshot 2025-09-08 030415.png', '78', 180, 82, '20 / 02 / 2005', 'Undergraduate', '6754440518', '2385774820291', '0814310336'),
    (193, 17, 'Asher Coleman', 'C:/players/team17/Screenshot 2025-08-24 222800.png', 1, 'C:/players/team17/Screenshot 2025-08-24 222800.png', '01', 176, 77, '17 / 08 / 2005', 'Undergraduate', '6614202267', '1433277278951', '0839339405'),
    (194, 17, 'Sawyer Bennett', 'C:/players/team17/Screenshot 2025-08-24 222805.png', 2, 'C:/players/team17/Screenshot 2025-08-24 222805.png', '40', 177, 72, '22 / 05 / 2005', 'Undergraduate', '6537973956', '1360355402900', '0901422807'),
    (195, 17, 'Jade Usman', 'C:/players/team17/Screenshot 2025-08-24 222825.png', 3, 'C:/players/team17/Screenshot 2025-08-24 222825.png', '31', 180, 72, '30 / 01 / 2004', 'Undergraduate', '6722198149', '2473489356368', '0867916526'),
    (196, 17, 'Vivian Fuller', 'C:/players/team17/Screenshot 2025-08-24 222831.png', 4, 'C:/players/team17/Screenshot 2025-08-24 222831.png', '10', 191, 95, '27 / 06 / 2003', 'Undergraduate', '6784229526', '1455006907988', '0907761165'),
    (197, 17, 'Levi Shaw', 'C:/players/team17/Screenshot 2025-08-24 222837.png', 5, 'C:/players/team17/Screenshot 2025-08-24 222837.png', '87', 186, 85, '15 / 06 / 2004', 'Undergraduate', '6579582863', '2360529380106', '0918644205'),
    (198, 17, 'Grace Young', 'C:/players/team17/Screenshot 2025-08-24 222843.png', 6, 'C:/players/team17/Screenshot 2025-08-24 222843.png', '02', 177, 72, '16 / 04 / 2003', 'Undergraduate', '6552731086', '1438055239881', '0869124025'),
    (199, 17, 'Isaac Tan', 'C:/players/team17/Screenshot 2025-08-24 222850.png', 7, 'C:/players/team17/Screenshot 2025-08-24 222850.png', '70', 164, 86, '13 / 11 / 2003', 'Undergraduate', '6678833616', '1450014911722', '0991192256'),
    (200, 17, 'Vivian Lane', 'C:/players/team17/Screenshot 2025-08-24 222855.png', 8, 'C:/players/team17/Screenshot 2025-08-24 222855.png', '05', 194, 69, '14 / 02 / 2004', 'Undergraduate', '6567751666', '2472954602972', '0829595328'),
    (201, 17, 'Theo Young', 'C:/players/team17/Screenshot 2025-08-24 222901.png', 9, 'C:/players/team17/Screenshot 2025-08-24 222901.png', '52', 192, 83, '29 / 10 / 2005', 'Undergraduate', '6638619870', '2430692101791', '0909045735'),
    (202, 17, 'Hazel Murphy', 'C:/players/team17/Screenshot 2025-08-24 222907.png', 10, 'C:/players/team17/Screenshot 2025-08-24 222907.png', '26', 186, 54, '21 / 09 / 2005', 'Undergraduate', '6775315929', '1424892413172', '0866124893'),
    (203, 17, 'Logan Murphy', 'C:/players/team17/Screenshot 2025-08-24 222915.png', 11, 'C:/players/team17/Screenshot 2025-08-24 222915.png', '46', 193, 87, '30 / 08 / 2003', 'Undergraduate', '6569181613', '2454896801850', '0640456923'),
    (204, 17, 'Iris Bennett', 'C:/players/team17/Screenshot 2025-08-24 222920.png', 12, 'C:/players/team17/Screenshot 2025-08-24 222920.png', '16', 182, 73, '21 / 09 / 2003', 'Undergraduate', '6539783681', '1479344804189', '0993054764'),
    (205, 18, 'Cole Carter', 'C:/players/team18/Screenshot 2025-08-24 223234.png', 1, 'C:/players/team18/Screenshot 2025-08-24 223234.png', '32', 164, 61, '31 / 08 / 2004', 'Undergraduate', '6718125251', '2490316341463', '0890260184'),
    (206, 18, 'Vivian Ibrahim', 'C:/players/team18/Screenshot 2025-08-24 223247.png', 2, 'C:/players/team18/Screenshot 2025-08-24 223247.png', '37', 168, 58, '10 / 06 / 2003', 'Undergraduate', '6629357913', '1376884795706', '0985405595'),
    (207, 18, 'Vera Cooper', 'C:/players/team18/Screenshot 2025-08-24 223251.png', 3, 'C:/players/team18/Screenshot 2025-08-24 223251.png', '59', 191, 85, '29 / 01 / 2005', 'Undergraduate', '6514552620', '1326978162634', '0898662036'),
    (208, 18, 'Opal Gray', 'C:/players/team18/Screenshot 2025-08-24 223259.png', 4, 'C:/players/team18/Screenshot 2025-08-24 223259.png', '06', 189, 68, '30 / 04 / 2003', 'Undergraduate', '6635639263', '1300470425291', '0965292081'),
    (209, 18, 'Jonah Valdez', 'C:/players/team18/Screenshot 2025-08-24 223306.png', 5, 'C:/players/team18/Screenshot 2025-08-24 223306.png', '38', 168, 68, '27 / 08 / 2005', 'Undergraduate', '6613162457', '1369045451455', '0657894414'),
    (210, 18, 'Caleb Bailey', 'C:/players/team18/Screenshot 2025-08-24 223312.png', 6, 'C:/players/team18/Screenshot 2025-08-24 223312.png', '05', 183, 77, '09 / 08 / 2003', 'Undergraduate', '6601267929', '1423626102020', '0642289833'),
    (211, 18, 'Casey Cohen', 'C:/players/team18/Screenshot 2025-08-24 223317.png', 7, 'C:/players/team18/Screenshot 2025-08-24 223317.png', '29', 181, 68, '21 / 04 / 2005', 'Undergraduate', '6703125868', '2477679973825', '0956222632'),
    (212, 18, 'Gabe D''''Angelo', 'C:/players/team18/Screenshot 2025-08-24 223322.png', 8, 'C:/players/team18/Screenshot 2025-08-24 223322.png', '42', 167, 50, '07 / 05 / 2005', 'Undergraduate', '6673030435', '2356837380501', '0840387800'),
    (213, 18, 'Tessa Edwards', 'C:/players/team18/Screenshot 2025-08-24 223327.png', 9, 'C:/players/team18/Screenshot 2025-08-24 223327.png', '26', 165, 93, '12 / 02 / 2003', 'Undergraduate', '6669639899', '2302911240433', '0699178864'),
    (214, 18, 'Blake Vega', 'C:/players/team18/Screenshot 2025-08-24 223332.png', 10, 'C:/players/team18/Screenshot 2025-08-24 223332.png', '41', 158, 98, '19 / 06 / 2003', 'Undergraduate', '6663819448', '2404139851794', '0959100186'),
    (215, 18, 'Maya Bailey', 'C:/players/team18/Screenshot 2025-08-24 223338.png', 11, 'C:/players/team18/Screenshot 2025-08-24 223338.png', '22', 169, 68, '08 / 04 / 2004', 'Undergraduate', '6514927545', '1369235402579', '0836498084'),
    (216, 18, 'Alex Edwards', 'C:/players/team18/Screenshot 2025-08-24 223341.png', 12, 'C:/players/team18/Screenshot 2025-08-24 223341.png', '90', 187, 68, '22 / 04 / 2005', 'Undergraduate', '6609145646', '2474603587123', '0678842631'),
    (217, 19, 'Clara Zhang', 'C:/players/team19/Screenshot 2025-08-24 223446.png', 1, 'C:/players/team19/Screenshot 2025-08-24 223446.png', '72', 186, 99, '04 / 05 / 2005', 'Undergraduate', '6683926783', '1478986062415', '0633880673'),
    (218, 19, 'Talon Tan', 'C:/players/team19/Screenshot 2025-08-24 223452.png', 2, 'C:/players/team19/Screenshot 2025-08-24 223452.png', '90', 185, 63, '29 / 06 / 2005', 'Undergraduate', '6728967216', '1388573877494', '0808733076'),
    (219, 19, 'Blake Holland', 'C:/players/team19/Screenshot 2025-08-24 223455.png', 3, 'C:/players/team19/Screenshot 2025-08-24 223455.png', '07', 166, 86, '30 / 11 / 2003', 'Undergraduate', '6503852827', '1329927983650', '0949828492'),
    (220, 19, 'Riley Young', 'C:/players/team19/Screenshot 2025-08-24 223502.png', 4, 'C:/players/team19/Screenshot 2025-08-24 223502.png', '37', 168, 73, '18 / 05 / 2003', 'Undergraduate', '6749272982', '2399243624184', '0678058201'),
    (221, 19, 'Kara Taylor', 'C:/players/team19/Screenshot 2025-08-24 223507.png', 5, 'C:/players/team19/Screenshot 2025-08-24 223507.png', '14', 181, 87, '16 / 06 / 2005', 'Undergraduate', '6771456631', '1433640418624', '0823074248'),
    (222, 19, 'Troy Hall', 'C:/players/team19/Screenshot 2025-08-24 223513.png', 6, 'C:/players/team19/Screenshot 2025-08-24 223513.png', '43', 183, 54, '01 / 11 / 2004', 'Undergraduate', '6616942440', '1465567286494', '0864712475'),
    (223, 19, 'Clara Reed', 'C:/players/team19/Screenshot 2025-08-24 223518.png', 7, 'C:/players/team19/Screenshot 2025-08-24 223518.png', '39', 175, 86, '17 / 12 / 2005', 'Undergraduate', '6673306172', '1466969700407', '0884342685'),
    (224, 19, 'Chase Rowe', 'C:/players/team19/Screenshot 2025-08-24 223522.png', 8, 'C:/players/team19/Screenshot 2025-08-24 223522.png', '57', 172, 99, '01 / 02 / 2003', 'Undergraduate', '6754864858', '1413728785533', '0835470678'),
    (225, 19, 'Wade Bailey', 'C:/players/team19/Screenshot 2025-08-24 223526.png', 9, 'C:/players/team19/Screenshot 2025-08-24 223526.png', '74', 180, 78, '03 / 02 / 2005', 'Undergraduate', '6531030233', '2378391576713', '0900550638'),
    (226, 19, 'Riley Zhang', 'C:/players/team19/Screenshot 2025-08-24 223529.png', 10, 'C:/players/team19/Screenshot 2025-08-24 223529.png', '76', 191, 59, '22 / 06 / 2003', 'Undergraduate', '6508419147', '2450076282671', '0608253236'),
    (227, 19, 'Riley Wong', 'C:/players/team19/Screenshot 2025-08-24 223534.png', 11, 'C:/players/team19/Screenshot 2025-08-24 223534.png', '87', 179, 55, '04 / 10 / 2003', 'Undergraduate', '6739145831', '1354321751263', '0810214328'),
    (228, 19, 'Blair Rowe', 'C:/players/team19/Screenshot 2025-08-24 223545.png', 12, 'C:/players/team19/Screenshot 2025-08-24 223545.png', '80', 192, 78, '01 / 02 / 2005', 'Undergraduate', '6603271105', '1375306648067', '0839240243'),
    (229, 20, 'Reed Nolan', 'C:/players/team20/Screenshot 2025-08-25 004434.png', 1, 'C:/players/team20/Screenshot 2025-08-25 004434.png', '10', 178, 80, '19 / 03 / 2004', 'Undergraduate', '6742532299', '2490962586504', '0920412555'),
    (230, 20, 'Blair Foster', 'C:/players/team20/Screenshot 2025-08-25 004437.png', 2, 'C:/players/team20/Screenshot 2025-08-25 004437.png', '40', 173, 63, '18 / 08 / 2003', 'Undergraduate', '6629547603', '2373807260220', '0933773218'),
    (231, 20, 'Opal Taylor', 'C:/players/team20/Screenshot 2025-08-25 004441.png', 3, 'C:/players/team20/Screenshot 2025-08-25 004441.png', '63', 180, 60, '25 / 04 / 2005', 'Undergraduate', '6558725153', '2350464226451', '0633987249'),
    (232, 20, 'Jonah Ross', 'C:/players/team20/Screenshot 2025-08-25 004444.png', 4, 'C:/players/team20/Screenshot 2025-08-25 004444.png', '28', 193, 57, '01 / 09 / 2005', 'Undergraduate', '6558885571', '2468371585643', '0912412816'),
    (233, 20, 'Iris Foster', 'C:/players/team20/Screenshot 2025-08-25 004448.png', 5, 'C:/players/team20/Screenshot 2025-08-25 004448.png', '78', 156, 99, '07 / 10 / 2005', 'Undergraduate', '6799911304', '2301178420179', '0806758983'),
    (234, 20, 'Ivy Brooks', 'C:/players/team20/Screenshot 2025-08-25 004450.png', 6, 'C:/players/team20/Screenshot 2025-08-25 004450.png', '71', 192, 74, '08 / 12 / 2004', 'Undergraduate', '6768584240', '2378244096075', '0621247341'),
    (235, 20, 'Alex Cooper', 'C:/players/team20/Screenshot 2025-08-25 004453.png', 7, 'C:/players/team20/Screenshot 2025-08-25 004453.png', '67', 162, 71, '31 / 08 / 2005', 'Undergraduate', '6548454902', '2391026489281', '0667872509'),
    (236, 20, 'Vera Anderson', 'C:/players/team20/Screenshot 2025-08-25 004456.png', 8, 'C:/players/team20/Screenshot 2025-08-25 004456.png', '93', 179, 64, '11 / 05 / 2003', 'Undergraduate', '6648135442', '2381627898607', '0672547479'),
    (237, 20, 'Sawyer Davis', 'C:/players/team20/Screenshot 2025-08-25 004459.png', 9, 'C:/players/team20/Screenshot 2025-08-25 004459.png', '90', 165, 57, '18 / 03 / 2004', 'Undergraduate', '6580729533', '2494901974184', '0676616790'),
    (238, 20, 'Noah Simmons', 'C:/players/team20/Screenshot 2025-08-25 004502.png', 10, 'C:/players/team20/Screenshot 2025-08-25 004502.png', '62', 194, 63, '20 / 12 / 2005', 'Undergraduate', '6756181126', '2380276995922', '0994685980'),
    (239, 20, 'Uriah Zhang', 'C:/players/team20/Screenshot 2025-08-25 004506.png', 11, 'C:/players/team20/Screenshot 2025-08-25 004506.png', '92', 187, 68, '22 / 02 / 2004', 'Undergraduate', '6537736394', '2416060599632', '0953830128'),
    (240, 20, 'Miles Griffin', 'C:/players/team20/Screenshot 2025-08-25 004510.png', 12, 'C:/players/team20/Screenshot 2025-08-25 004510.png', '72', 180, 50, '29 / 04 / 2005', 'Undergraduate', '6770482268', '1489799071113', '0858251050'),
    (241, 21, 'Dominic Larson', 'C:/players/team21/Screenshot 2025-08-25 010501.png', 1, 'C:/players/team21/Screenshot 2025-08-25 010501.png', '14', 165, 96, '14 / 11 / 2005', 'Undergraduate', '6636597384', '1326726024504', '0603954560'),
    (242, 21, 'Elias Vargas', 'C:/players/team21/Screenshot 2025-08-25 010508.png', 2, 'C:/players/team21/Screenshot 2025-08-25 010508.png', '40', 185, 98, '04 / 01 / 2004', 'Undergraduate', '6754045749', '2442160053506', '0954589897'),
    (243, 21, 'Omar Bennett', 'C:/players/team21/Screenshot 2025-08-25 010512.png', 3, 'C:/players/team21/Screenshot 2025-08-25 010512.png', '67', 163, 69, '18 / 09 / 2003', 'Undergraduate', '6585863681', '1469579357638', '0642673972'),
    (244, 21, 'Jade Valdez', 'C:/players/team21/Screenshot 2025-08-25 010517 - Copy.png', 4, 'C:/players/team21/Screenshot 2025-08-25 010517 - Copy.png', '61', 171, 91, '05 / 09 / 2004', 'Undergraduate', '6780161729', '2494352141383', '0853470697'),
    (245, 21, 'Hannah Fuller', 'C:/players/team21/Screenshot 2025-08-25 010517.png', 5, 'C:/players/team21/Screenshot 2025-08-25 010517.png', '64', 172, 51, '02 / 01 / 2003', 'Undergraduate', '6735609354', '2411290018645', '0984960232'),
    (246, 21, 'Xander Clark', 'C:/players/team21/Screenshot 2025-08-25 010521.png', 6, 'C:/players/team21/Screenshot 2025-08-25 010521.png', '16', 177, 58, '28 / 07 / 2005', 'Undergraduate', '6651674902', '2300186549320', '0867983829'),
    (247, 21, 'Zara Zimmerman', 'C:/players/team21/Screenshot 2025-08-25 010524.png', 7, 'C:/players/team21/Screenshot 2025-08-25 010524.png', '81', 155, 52, '11 / 10 / 2005', 'Undergraduate', '6632315863', '2343505900544', '0647275781'),
    (248, 21, 'Omar Gray', 'C:/players/team21/Screenshot 2025-08-25 010530.png', 8, 'C:/players/team21/Screenshot 2025-08-25 010530.png', '86', 192, 92, '07 / 12 / 2005', 'Undergraduate', '6539073864', '1358444094787', '0850072435'),
    (249, 21, 'Zayne Jenkins', 'C:/players/team21/Screenshot 2025-08-25 010532.png', 9, 'C:/players/team21/Screenshot 2025-08-25 010532.png', '04', 193, 87, '29 / 05 / 2004', 'Undergraduate', '6514590276', '1482707204344', '0604859891'),
    (250, 21, 'Naomi Parker', 'C:/players/team21/Screenshot 2025-08-25 010535.png', 10, 'C:/players/team21/Screenshot 2025-08-25 010535.png', '46', 170, 70, '04 / 02 / 2003', 'Undergraduate', '6632123438', '1490098507529', '0685226638'),
    (251, 21, 'Zayne Xu', 'C:/players/team21/Screenshot 2025-08-25 010537.png', 11, 'C:/players/team21/Screenshot 2025-08-25 010537.png', '70', 157, 81, '15 / 04 / 2005', 'Undergraduate', '6680612931', '2459022592882', '0662894203'),
    (252, 21, 'Keira Bishop', 'C:/players/team21/Screenshot 2025-08-25 010540.png', 12, 'C:/players/team21/Screenshot 2025-08-25 010540.png', '88', 195, 66, '18 / 01 / 2004', 'Undergraduate', '6513711103', '1423731142931', '0988766461'),
    (253, 22, 'Sienna Carter', 'C:/players/team22/Screenshot 2025-08-25 011707.png', 1, 'C:/players/team22/Screenshot 2025-08-25 011707.png', '10', 171, 64, '10 / 02 / 2005', 'Undergraduate', '6715499087', '1427886699241', '0927138195'),
    (254, 22, 'Asher Shaw', 'C:/players/team22/Screenshot 2025-08-25 011710.png', 2, 'C:/players/team22/Screenshot 2025-08-25 011710.png', '07', 184, 84, '13 / 01 / 2004', 'Undergraduate', '6739186015', '2463643691303', '0889563404'),
    (255, 22, 'Violet Nolan', 'C:/players/team22/Screenshot 2025-08-25 011714.png', 3, 'C:/players/team22/Screenshot 2025-08-25 011714.png', '50', 184, 89, '11 / 09 / 2003', 'Undergraduate', '6583273576', '1373484972471', '0896160153'),
    (256, 22, 'Talon Ortiz', 'C:/players/team22/Screenshot 2025-08-25 011717.png', 4, 'C:/players/team22/Screenshot 2025-08-25 011717.png', '03', 184, 79, '08 / 07 / 2005', 'Undergraduate', '6759470372', '1337722450691', '0928345717'),
    (257, 22, 'Faith Chung', 'C:/players/team22/Screenshot 2025-08-25 011720.png', 5, 'C:/players/team22/Screenshot 2025-08-25 011720.png', '21', 155, 59, '27 / 02 / 2005', 'Undergraduate', '6636755688', '2300452488111', '0853053080'),
    (258, 22, 'Owen Lane', 'C:/players/team22/Screenshot 2025-08-25 011723.png', 6, 'C:/players/team22/Screenshot 2025-08-25 011723.png', '97', 163, 94, '12 / 08 / 2003', 'Undergraduate', '6513245979', '2487669879222', '0659867080'),
    (259, 22, 'Uma Chung', 'C:/players/team22/Screenshot 2025-08-25 011725.png', 7, 'C:/players/team22/Screenshot 2025-08-25 011725.png', '74', 196, 86, '14 / 01 / 2004', 'Undergraduate', '6526422968', '1357795920476', '0944838562'),
    (260, 22, 'Asher Diaz', 'C:/players/team22/Screenshot 2025-08-25 011729.png', 8, 'C:/players/team22/Screenshot 2025-08-25 011729.png', '11', 163, 95, '17 / 04 / 2003', 'Undergraduate', '6505029358', '2482777588140', '0643563710'),
    (261, 22, 'Kylie Usman', 'C:/players/team22/Screenshot 2025-08-25 011732.png', 9, 'C:/players/team22/Screenshot 2025-08-25 011732.png', '28', 165, 79, '23 / 10 / 2003', 'Undergraduate', '6777931591', '1355250603284', '0969479238'),
    (262, 22, 'Troy Xu', 'C:/players/team22/Screenshot 2025-08-25 011735.png', 10, 'C:/players/team22/Screenshot 2025-08-25 011735.png', '77', 165, 80, '17 / 07 / 2005', 'Undergraduate', '6661117564', '2471341550721', '0642432369'),
    (263, 22, 'Riley Ross', 'C:/players/team22/Screenshot 2025-08-25 011737.png', 11, 'C:/players/team22/Screenshot 2025-08-25 011737.png', '98', 174, 66, '14 / 06 / 2003', 'Undergraduate', '6582180789', '2463355711112', '0645789438'),
    (264, 22, 'Logan Peterson', 'C:/players/team22/Screenshot 2025-08-25 011740.png', 12, 'C:/players/team22/Screenshot 2025-08-25 011740.png', '96', 163, 99, '21 / 12 / 2003', 'Undergraduate', '6658682749', '2372582217721', '0992950195'),
    (265, 23, 'Riley Rogers', 'C:/players/team23/Screenshot 2025-08-25 011945.png', 1, 'C:/players/team23/Screenshot 2025-08-25 011945.png', '86', 162, 98, '18 / 10 / 2005', 'Undergraduate', '6794514822', '2430479896651', '0897179896'),
    (266, 23, 'Georgia Patel', 'C:/players/team23/Screenshot 2025-08-25 011947.png', 2, 'C:/players/team23/Screenshot 2025-08-25 011947.png', '11', 168, 70, '27 / 09 / 2005', 'Undergraduate', '6530041563', '2399734027500', '0866462157'),
    (267, 23, 'Kai Xu', 'C:/players/team23/Screenshot 2025-08-25 011950.png', 3, 'C:/players/team23/Screenshot 2025-08-25 011950.png', '99', 188, 87, '05 / 03 / 2004', 'Undergraduate', '6515128576', '2303380438646', '0615737115'),
    (268, 23, 'Zayne Henderson', 'C:/players/team23/Screenshot 2025-08-25 011953.png', 4, 'C:/players/team23/Screenshot 2025-08-25 011953.png', '94', 179, 75, '10 / 11 / 2003', 'Undergraduate', '6581798541', '1333754052450', '0697905234'),
    (269, 23, 'Owen Clark', 'C:/players/team23/Screenshot 2025-08-25 011956.png', 5, 'C:/players/team23/Screenshot 2025-08-25 011956.png', '51', 173, 79, '22 / 05 / 2003', 'Undergraduate', '6513337234', '2320381023633', '0801747762'),
    (270, 23, 'Hayden Usman', 'C:/players/team23/Screenshot 2025-08-25 011958.png', 6, 'C:/players/team23/Screenshot 2025-08-25 011958.png', '96', 169, 84, '17 / 10 / 2004', 'Undergraduate', '6745283845', '2336349663784', '0615863147'),
    (271, 23, 'Naomi Ward', 'C:/players/team23/Screenshot 2025-08-25 012001.png', 7, 'C:/players/team23/Screenshot 2025-08-25 012001.png', '73', 184, 57, '22 / 05 / 2004', 'Undergraduate', '6678796837', '1375051479818', '0645765316'),
    (272, 23, 'Theo Holland', 'C:/players/team23/Screenshot 2025-08-25 012003.png', 8, 'C:/players/team23/Screenshot 2025-08-25 012003.png', '75', 194, 91, '22 / 02 / 2005', 'Undergraduate', '6595993450', '1423068382089', '0672430781'),
    (273, 23, 'Parker Edwards', 'C:/players/team23/Screenshot 2025-08-25 012006.png', 9, 'C:/players/team23/Screenshot 2025-08-25 012006.png', '03', 193, 95, '19 / 09 / 2003', 'Undergraduate', '6631240186', '2459566150213', '0891786434'),
    (274, 23, 'Liam Rossi', 'C:/players/team23/Screenshot 2025-08-25 012008.png', 10, 'C:/players/team23/Screenshot 2025-08-25 012008.png', '66', 183, 60, '04 / 10 / 2004', 'Undergraduate', '6754363220', '2321704954901', '0810115094'),
    (275, 23, 'Wade Bishop', 'C:/players/team23/Screenshot 2025-08-25 012010.png', 11, 'C:/players/team23/Screenshot 2025-08-25 012010.png', '59', 194, 65, '08 / 09 / 2005', 'Undergraduate', '6710197899', '2467908187181', '0964570776'),
    (276, 23, 'Isaac Cooper', 'C:/players/team23/Screenshot 2025-08-25 012013.png', 12, 'C:/players/team23/Screenshot 2025-08-25 012013.png', '78', 192, 91, '16 / 09 / 2005', 'Undergraduate', '6552108695', '1478233818679', '0608867339'),
    (277, 24, 'Naomi Usman', 'C:/players/team24/Screenshot 2025-08-25 012335.png', 1, 'C:/players/team24/Screenshot 2025-08-25 012335.png', '05', 195, 64, '04 / 07 / 2003', 'Undergraduate', '6694518048', '1496264696735', '0689545273'),
    (278, 24, 'Sage Nguyen', 'C:/players/team24/Screenshot 2025-08-25 012337.png', 2, 'C:/players/team24/Screenshot 2025-08-25 012337.png', '54', 192, 98, '05 / 05 / 2005', 'Undergraduate', '6517285523', '1400902330041', '0843842637'),
    (279, 24, 'Iris Chung', 'C:/players/team24/Screenshot 2025-08-25 012340.png', 3, 'C:/players/team24/Screenshot 2025-08-25 012340.png', '43', 158, 97, '22 / 08 / 2003', 'Undergraduate', '6720344962', '2487132784725', '0965106960'),
    (280, 24, 'Elena Rogers', 'C:/players/team24/Screenshot 2025-08-25 012344.png', 4, 'C:/players/team24/Screenshot 2025-08-25 012344.png', '32', 199, 95, '06 / 02 / 2005', 'Undergraduate', '6796292222', '1388152191715', '0912581477'),
    (281, 24, 'Sienna Jordan', 'C:/players/team24/Screenshot 2025-08-25 012348.png', 5, 'C:/players/team24/Screenshot 2025-08-25 012348.png', '30', 179, 87, '24 / 10 / 2003', 'Undergraduate', '6672992853', '2498792021835', '0683798880'),
    (282, 24, 'Will Jenkins', 'C:/players/team24/Screenshot 2025-08-25 012351.png', 6, 'C:/players/team24/Screenshot 2025-08-25 012351.png', '24', 190, 92, '08 / 04 / 2003', 'Undergraduate', '6610779606', '1405014589779', '0939505918'),
    (283, 24, 'Georgia Ramirez', 'C:/players/team24/Screenshot 2025-08-25 012354.png', 7, 'C:/players/team24/Screenshot 2025-08-25 012354.png', '38', 171, 84, '07 / 04 / 2005', 'Undergraduate', '6620607913', '1477825708398', '0625896846'),
    (284, 24, 'Blake Barnes', 'C:/players/team24/Screenshot 2025-08-25 012359.png', 8, 'C:/players/team24/Screenshot 2025-08-25 012359.png', '61', 194, 65, '31 / 01 / 2005', 'Undergraduate', '6745162375', '2496459299211', '0997465837'),
    (285, 24, 'Jade Davis', 'C:/players/team24/Screenshot 2025-08-25 012402.png', 9, 'C:/players/team24/Screenshot 2025-08-25 012402.png', '09', 189, 76, '18 / 06 / 2003', 'Undergraduate', '6770208918', '2338210991551', '0699178426'),
    (286, 24, 'Faith Vargas', 'C:/players/team24/Screenshot 2025-08-25 012407.png', 10, 'C:/players/team24/Screenshot 2025-08-25 012407.png', '47', 196, 74, '30 / 09 / 2003', 'Undergraduate', '6787649666', '1407264261250', '0657224541'),
    (287, 24, 'Vivian Rivera', 'C:/players/team24/Screenshot 2025-08-25 012410.png', 11, 'C:/players/team24/Screenshot 2025-08-25 012410.png', '58', 200, 80, '17 / 03 / 2005', 'Undergraduate', '6780688642', '1458594889318', '0692912273'),
    (288, 24, 'Hannah Patterson', 'C:/players/team24/Screenshot 2025-08-25 012414.png', 12, 'C:/players/team24/Screenshot 2025-08-25 012414.png', '94', 189, 84, '15 / 08 / 2003', 'Undergraduate', '6542865776', '2342337348796', '0871470243'),
    (289, 25, 'Quincy Holland', 'C:/players/team25/Screenshot 2025-08-25 012920.png', 1, 'C:/players/team25/Screenshot 2025-08-25 012920.png', '26', 183, 76, '26 / 09 / 2004', 'Undergraduate', '6732798265', '1451109015962', '0608977006'),
    (290, 25, 'Skye Davis', 'C:/players/team25/Screenshot 2025-08-25 012923.png', 2, 'C:/players/team25/Screenshot 2025-08-25 012923.png', '30', 165, 72, '26 / 12 / 2005', 'Undergraduate', '6780663013', '1412397769152', '0652318699'),
    (291, 25, 'Hunter Usman', 'C:/players/team25/Screenshot 2025-08-25 012926.png', 3, 'C:/players/team25/Screenshot 2025-08-25 012926.png', '24', 167, 76, '08 / 11 / 2005', 'Undergraduate', '6796173115', '1300751528515', '0652827019'),
    (292, 25, 'Omar Cooper', 'C:/players/team25/Screenshot 2025-08-25 012928.png', 4, 'C:/players/team25/Screenshot 2025-08-25 012928.png', '99', 194, 75, '10 / 11 / 2005', 'Undergraduate', '6519428104', '1494035177673', '0891104698'),
    (293, 25, 'Will Griffin', 'C:/players/team25/Screenshot 2025-08-25 012931.png', 5, 'C:/players/team25/Screenshot 2025-08-25 012931.png', '05', 155, 66, '26 / 05 / 2005', 'Undergraduate', '6664644388', '1428357241152', '0919921802'),
    (294, 25, 'Owen Zhang', 'C:/players/team25/Screenshot 2025-08-25 012933.png', 6, 'C:/players/team25/Screenshot 2025-08-25 012933.png', '94', 177, 84, '28 / 02 / 2004', 'Undergraduate', '6533594410', '2462596262064', '0815219256'),
    (295, 25, 'Rowan Davis', 'C:/players/team25/Screenshot 2025-08-25 012936.png', 7, 'C:/players/team25/Screenshot 2025-08-25 012936.png', '80', 157, 51, '05 / 02 / 2003', 'Undergraduate', '6790949805', '2328899089594', '0812717934'),
    (296, 25, 'Will Owens', 'C:/players/team25/Screenshot 2025-08-25 012940.png', 8, 'C:/players/team25/Screenshot 2025-08-25 012940.png', '03', 177, 77, '29 / 02 / 2004', 'Undergraduate', '6581803632', '1305635814781', '0629790988'),
    (297, 25, 'Wade Quinn', 'C:/players/team25/Screenshot 2025-08-25 012944.png', 9, 'C:/players/team25/Screenshot 2025-08-25 012944.png', '32', 174, 96, '10 / 03 / 2003', 'Undergraduate', '6776889567', '2337595944914', '0992078903'),
    (298, 25, 'Yara Kim', 'C:/players/team25/Screenshot 2025-08-25 012948.png', 10, 'C:/players/team25/Screenshot 2025-08-25 012948.png', '29', 181, 62, '31 / 03 / 2003', 'Undergraduate', '6661113179', '2430408483655', '0920074039'),
    (299, 25, 'Kylie Lane', 'C:/players/team25/Screenshot 2025-08-25 012952.png', 11, 'C:/players/team25/Screenshot 2025-08-25 012952.png', '06', 179, 50, '15 / 06 / 2005', 'Undergraduate', '6787860069', '2395657569478', '0950530738'),
    (300, 25, 'Clara Foster', 'C:/players/team25/Screenshot 2025-08-25 012956.png', 12, 'C:/players/team25/Screenshot 2025-08-25 012956.png', '34', 195, 66, '27 / 10 / 2005', 'Undergraduate', '6698889569', '1403333607314', '0955570384'),
    (301, 26, 'Sienna Lane', 'C:/players/team26/Screenshot 2025-08-25 013558.png', 1, 'C:/players/team26/Screenshot 2025-08-25 013558.png', '29', 176, 92, '04 / 04 / 2005', 'Undergraduate', '6717898175', '2413460161259', '0943537506'),
    (302, 26, 'Jasper Wood', 'C:/players/team26/Screenshot 2025-08-25 013603.png', 2, 'C:/players/team26/Screenshot 2025-08-25 013603.png', '11', 181, 88, '17 / 01 / 2004', 'Undergraduate', '6710503238', '2463921459730', '0993891564'),
    (303, 26, 'Xander Griffin', 'C:/players/team26/Screenshot 2025-08-25 013608.png', 3, 'C:/players/team26/Screenshot 2025-08-25 013608.png', '22', 162, 92, '03 / 07 / 2003', 'Undergraduate', '6573479771', '2439652663509', '0818916607'),
    (304, 26, 'Mason Wood', 'C:/players/team26/Screenshot 2025-08-25 013611.png', 4, 'C:/players/team26/Screenshot 2025-08-25 013611.png', '44', 193, 93, '14 / 02 / 2003', 'Undergraduate', '6798387633', '1369476748678', '0873758975'),
    (305, 26, 'Aria Patterson', 'C:/players/team26/Screenshot 2025-08-25 013615.png', 5, 'C:/players/team26/Screenshot 2025-08-25 013615.png', '87', 166, 55, '20 / 06 / 2005', 'Undergraduate', '6731783510', '1433958460270', '0935642776'),
    (306, 26, 'Levi Wong', 'C:/players/team26/Screenshot 2025-08-25 013618.png', 6, 'C:/players/team26/Screenshot 2025-08-25 013618.png', '90', 185, 82, '30 / 06 / 2003', 'Undergraduate', '6526107400', '2485069537523', '0840984701'),
    (307, 26, 'Skye Foster', 'C:/players/team26/Screenshot 2025-08-25 013621.png', 7, 'C:/players/team26/Screenshot 2025-08-25 013621.png', '89', 179, 84, '27 / 03 / 2003', 'Undergraduate', '6657542341', '2375091243490', '0860336035'),
    (308, 26, 'Eli Quezada', 'C:/players/team26/Screenshot 2025-08-25 013624.png', 8, 'C:/players/team26/Screenshot 2025-08-25 013624.png', '97', 198, 53, '16 / 03 / 2003', 'Undergraduate', '6645539307', '2413886046250', '0678192364'),
    (309, 26, 'Wren Griffin', 'C:/players/team26/Screenshot 2025-08-25 013628.png', 9, 'C:/players/team26/Screenshot 2025-08-25 013628.png', '54', 190, 95, '12 / 03 / 2003', 'Undergraduate', '6791065314', '2300382071721', '0680804634'),
    (310, 26, 'Yara Hughes', 'C:/players/team26/Screenshot 2025-08-25 013631.png', 10, 'C:/players/team26/Screenshot 2025-08-25 013631.png', '37', 171, 51, '19 / 01 / 2005', 'Undergraduate', '6597697261', '2371260712307', '0684734828'),
    (311, 26, 'Maddox Zimmerman', 'C:/players/team26/Screenshot 2025-08-25 013633.png', 11, 'C:/players/team26/Screenshot 2025-08-25 013633.png', '61', 192, 56, '27 / 08 / 2004', 'Undergraduate', '6694976668', '2452604638757', '0927583740'),
    (312, 26, 'June Wood', 'C:/players/team26/Screenshot 2025-08-25 013636.png', 12, 'C:/players/team26/Screenshot 2025-08-25 013636.png', '55', 200, 97, '21 / 01 / 2005', 'Undergraduate', '6629453042', '2344042460007', '0964252624'),
    (313, 27, 'Trent Barker', 'C:/players/team27/Screenshot 2025-08-25 014216.png', 1, 'C:/players/team27/Screenshot 2025-08-25 014216.png', '41', 167, 81, '23 / 10 / 2005', 'Undergraduate', '6559201067', '2371745004568', '0999696490'),
    (314, 27, 'Wade Cook', 'C:/players/team27/Screenshot 2025-08-25 014219.png', 2, 'C:/players/team27/Screenshot 2025-08-25 014219.png', '28', 192, 79, '26 / 06 / 2005', 'Undergraduate', '6656042804', '2365621941547', '0676278634'),
    (315, 27, 'Derek Cole', 'C:/players/team27/Screenshot 2025-08-25 014223.png', 3, 'C:/players/team27/Screenshot 2025-08-25 014223.png', '58', 180, 63, '09 / 12 / 2004', 'Undergraduate', '6747530339', '1421977172771', '0682221660'),
    (316, 27, 'Hannah Xu', 'C:/players/team27/Screenshot 2025-08-25 014225.png', 4, 'C:/players/team27/Screenshot 2025-08-25 014225.png', '18', 174, 95, '12 / 02 / 2005', 'Undergraduate', '6738419872', '1304688552543', '0694639257'),
    (317, 27, 'Jay Patterson', 'C:/players/team27/Screenshot 2025-08-25 014230.png', 5, 'C:/players/team27/Screenshot 2025-08-25 014230.png', '99', 190, 99, '08 / 11 / 2004', 'Undergraduate', '6525292110', '2342793872869', '0809648900'),
    (318, 27, 'Tessa Hughes', 'C:/players/team27/Screenshot 2025-08-25 014235.png', 6, 'C:/players/team27/Screenshot 2025-08-25 014235.png', '82', 184, 56, '23 / 07 / 2003', 'Undergraduate', '6587450297', '2429087720249', '0644899697'),
    (319, 27, 'Theo Rowe', 'C:/players/team27/Screenshot 2025-08-25 014239.png', 7, 'C:/players/team27/Screenshot 2025-08-25 014239.png', '08', 182, 66, '03 / 03 / 2004', 'Undergraduate', '6560285785', '1355837490707', '0610411237'),
    (320, 27, 'Keira Yamamoto', 'C:/players/team27/Screenshot 2025-08-25 014242.png', 8, 'C:/players/team27/Screenshot 2025-08-25 014242.png', '31', 183, 65, '09 / 05 / 2005', 'Undergraduate', '6697213292', '2421819157248', '0668696338'),
    (321, 27, 'Iris Taylor', 'C:/players/team27/Screenshot 2025-08-25 014245.png', 9, 'C:/players/team27/Screenshot 2025-08-25 014245.png', '72', 158, 77, '16 / 02 / 2003', 'Undergraduate', '6557372625', '2350731516277', '0957093497'),
    (322, 27, 'Lola Price', 'C:/players/team27/Screenshot 2025-08-25 014248.png', 10, 'C:/players/team27/Screenshot 2025-08-25 014248.png', '25', 170, 93, '07 / 07 / 2005', 'Undergraduate', '6754296259', '2450364751501', '0800161170'),
    (323, 27, 'Skye Nguyen', 'C:/players/team27/Screenshot 2025-08-25 014250.png', 11, 'C:/players/team27/Screenshot 2025-08-25 014250.png', '35', 172, 79, '10 / 04 / 2005', 'Undergraduate', '6776873668', '1387232656951', '0898062908'),
    (324, 27, 'Felix Vega', 'C:/players/team27/Screenshot 2025-08-25 014253.png', 12, 'C:/players/team27/Screenshot 2025-08-25 014253.png', '81', 161, 84, '08 / 02 / 2003', 'Undergraduate', '6658134379', '1384801943956', '0917398572'),
    (325, 28, 'Troy Ramirez', 'C:/players/team28/Screenshot 2025-08-25 015011.png', 1, 'C:/players/team28/Screenshot 2025-08-25 015011.png', '86', 199, 71, '04 / 05 / 2004', 'Undergraduate', '6645247282', '1408055288229', '0894585315'),
    (326, 28, 'Faith Rossi', 'C:/players/team28/Screenshot 2025-08-25 015014.png', 2, 'C:/players/team28/Screenshot 2025-08-25 015014.png', '21', 165, 78, '24 / 11 / 2003', 'Undergraduate', '6511840983', '1395832573434', '0948079884'),
    (327, 28, 'Theo Coleman', 'C:/players/team28/Screenshot 2025-08-25 015017.png', 3, 'C:/players/team28/Screenshot 2025-08-25 015017.png', '64', 194, 81, '18 / 01 / 2003', 'Undergraduate', '6769801006', '2307463545621', '0638696101'),
    (328, 28, 'Rowan Vega', 'C:/players/team28/Screenshot 2025-08-25 015020.png', 4, 'C:/players/team28/Screenshot 2025-08-25 015020.png', '16', 173, 65, '20 / 08 / 2004', 'Undergraduate', '6669611189', '2348225434777', '0693706112'),
    (329, 28, 'Lena Valdez', 'C:/players/team28/Screenshot 2025-08-25 015024.png', 5, 'C:/players/team28/Screenshot 2025-08-25 015024.png', '61', 196, 55, '18 / 12 / 2005', 'Undergraduate', '6732940725', '2443476401785', '0898572490'),
    (330, 28, 'Emma Diaz', 'C:/players/team28/Screenshot 2025-08-25 015027.png', 6, 'C:/players/team28/Screenshot 2025-08-25 015027.png', '70', 157, 64, '02 / 07 / 2003', 'Undergraduate', '6748219983', '2361664335670', '0961034981'),
    (331, 28, 'Naomi Smith', 'C:/players/team28/Screenshot 2025-08-25 015030.png', 7, 'C:/players/team28/Screenshot 2025-08-25 015030.png', '26', 176, 99, '22 / 04 / 2003', 'Undergraduate', '6724745263', '2441255164592', '0950335713'),
    (332, 28, 'Zara Young', 'C:/players/team28/Screenshot 2025-08-25 015035.png', 8, 'C:/players/team28/Screenshot 2025-08-25 015035.png', '30', 187, 93, '08 / 06 / 2004', 'Undergraduate', '6654040431', '2423147841912', '0934588246'),
    (333, 28, 'Theo Yamamoto', 'C:/players/team28/Screenshot 2025-08-25 015038.png', 9, 'C:/players/team28/Screenshot 2025-08-25 015038.png', '40', 185, 91, '21 / 03 / 2003', 'Undergraduate', '6528079401', '1353921083813', '0675220849'),
    (334, 28, 'Liam Patterson', 'C:/players/team28/Screenshot 2025-08-25 015044.png', 10, 'C:/players/team28/Screenshot 2025-08-25 015044.png', '78', 198, 50, '24 / 08 / 2004', 'Undergraduate', '6532193931', '1356439326533', '0640332572'),
    (335, 28, 'Ivy O''''Connor', 'C:/players/team28/Screenshot 2025-08-25 015048.png', 11, 'C:/players/team28/Screenshot 2025-08-25 015048.png', '69', 172, 51, '01 / 02 / 2004', 'Undergraduate', '6550867862', '1393252924442', '0956371343'),
    (336, 28, 'Sienna Bennett', 'C:/players/team28/Screenshot 2025-08-25 015052.png', 12, 'C:/players/team28/Screenshot 2025-08-25 015052.png', '15', 181, 79, '07 / 08 / 2004', 'Undergraduate', '6536846043', '1382093252053', '0822960520'),
    (337, 29, 'Rowan Foster', 'C:/players/team29/Screenshot 2025-08-25 021127.png', 1, 'C:/players/team29/Screenshot 2025-08-25 021127.png', '58', 167, 64, '29 / 05 / 2003', 'Undergraduate', '6601871131', '1383680176509', '0900768186'),
    (338, 29, 'Dominic Rivera', 'C:/players/team29/Screenshot 2025-08-25 021129.png', 2, 'C:/players/team29/Screenshot 2025-08-25 021129.png', '34', 184, 58, '15 / 12 / 2003', 'Undergraduate', '6504608643', '2443238425024', '0637243600'),
    (339, 29, 'Jude Flores', 'C:/players/team29/Screenshot 2025-08-25 021132.png', 3, 'C:/players/team29/Screenshot 2025-08-25 021132.png', '06', 191, 85, '02 / 02 / 2005', 'Undergraduate', '6737920814', '1366436759412', '0893936008'),
    (340, 29, 'June Davis', 'C:/players/team29/Screenshot 2025-08-25 021134.png', 4, 'C:/players/team29/Screenshot 2025-08-25 021134.png', '65', 197, 77, '17 / 12 / 2004', 'Undergraduate', '6518528700', '2369118732643', '0616406426'),
    (341, 29, 'Logan Irwin', 'C:/players/team29/Screenshot 2025-08-25 021138.png', 5, 'C:/players/team29/Screenshot 2025-08-25 021138.png', '55', 155, 50, '27 / 11 / 2003', 'Undergraduate', '6579451029', '2371757828056', '0962648886'),
    (342, 29, 'Sienna Vega', 'C:/players/team29/Screenshot 2025-08-25 021141.png', 6, 'C:/players/team29/Screenshot 2025-08-25 021141.png', '57', 185, 83, '27 / 05 / 2005', 'Undergraduate', '6701506172', '1455201091045', '0915484477'),
    (343, 29, 'Wren Clark', 'C:/players/team29/Screenshot 2025-08-25 021144.png', 7, 'C:/players/team29/Screenshot 2025-08-25 021144.png', '30', 160, 93, '27 / 01 / 2005', 'Undergraduate', '6687120103', '2322491934594', '0914798820'),
    (344, 29, 'Maddox Mitchell', 'C:/players/team29/Screenshot 2025-08-25 021151.png', 8, 'C:/players/team29/Screenshot 2025-08-25 021151.png', '85', 194, 70, '17 / 09 / 2004', 'Undergraduate', '6714203857', '2422822850715', '0850770605'),
    (345, 29, 'Zayne Bennett', 'C:/players/team29/Screenshot 2025-08-25 021154.png', 9, 'C:/players/team29/Screenshot 2025-08-25 021154.png', '79', 196, 61, '12 / 09 / 2005', 'Undergraduate', '6662081534', '2348799114058', '0893690966'),
    (346, 29, 'Sawyer Mitchell', 'C:/players/team29/Screenshot 2025-08-25 021158.png', 10, 'C:/players/team29/Screenshot 2025-08-25 021158.png', '68', 172, 75, '21 / 12 / 2005', 'Undergraduate', '6612942394', '1453799655764', '0654717514'),
    (347, 29, 'Hazel Ng', 'C:/players/team29/Screenshot 2025-08-25 021200.png', 11, 'C:/players/team29/Screenshot 2025-08-25 021200.png', '91', 164, 94, '12 / 05 / 2005', 'Undergraduate', '6560883062', '1404602216913', '0950072937'),
    (348, 29, 'Blair Yates', 'C:/players/team29/Screenshot 2025-08-25 021203.png', 12, 'C:/players/team29/Screenshot 2025-08-25 021203.png', '80', 192, 67, '20 / 11 / 2003', 'Undergraduate', '6614304026', '1380664320339', '0855049127'),
    (349, 30, 'Brooke Miller', 'C:/players/team30/Screenshot 2025-08-25 024511.png', 1, 'C:/players/team30/Screenshot 2025-08-25 024511.png', '32', 197, 61, '11 / 04 / 2005', 'Undergraduate', '6502999761', '2379791705236', '0999909198'),
    (350, 30, 'Jasper Ibrahim', 'C:/players/team30/Screenshot 2025-08-25 024514.png', 2, 'C:/players/team30/Screenshot 2025-08-25 024514.png', '21', 184, 82, '09 / 11 / 2003', 'Undergraduate', '6599914078', '1355687374651', '0806976486'),
    (351, 30, 'Avery Mehta', 'C:/players/team30/Screenshot 2025-08-25 024516.png', 3, 'C:/players/team30/Screenshot 2025-08-25 024516.png', '34', 161, 82, '07 / 07 / 2004', 'Undergraduate', '6709715878', '1438760868249', '0864345961'),
    (352, 30, 'Wade Vega', 'C:/players/team30/Screenshot 2025-08-25 024519.png', 4, 'C:/players/team30/Screenshot 2025-08-25 024519.png', '08', 157, 71, '12 / 04 / 2005', 'Undergraduate', '6600673393', '2444253915542', '0833556172'),
    (353, 30, 'Hannah Foster', 'C:/players/team30/Screenshot 2025-08-25 024522.png', 5, 'C:/players/team30/Screenshot 2025-08-25 024522.png', '54', 175, 55, '08 / 01 / 2003', 'Undergraduate', '6622343989', '1438382541628', '0992594435'),
    (354, 30, 'Clara Bailey', 'C:/players/team30/Screenshot 2025-08-25 024526.png', 6, 'C:/players/team30/Screenshot 2025-08-25 024526.png', '16', 173, 52, '29 / 03 / 2003', 'Undergraduate', '6729640470', '2496572735977', '0686791044'),
    (355, 30, 'Jonah Howard', 'C:/players/team30/Screenshot 2025-08-25 024529.png', 7, 'C:/players/team30/Screenshot 2025-08-25 024529.png', '24', 194, 75, '04 / 07 / 2004', 'Undergraduate', '6515721224', '1480189701891', '0604355259'),
    (356, 30, 'Dana Edwards', 'C:/players/team30/Screenshot 2025-08-25 024531.png', 8, 'C:/players/team30/Screenshot 2025-08-25 024531.png', '53', 167, 95, '09 / 06 / 2005', 'Undergraduate', '6642964345', '2449726972607', '0668222536'),
    (357, 30, 'Alex D''''Angelo', 'C:/players/team30/Screenshot 2025-08-25 024536.png', 9, 'C:/players/team30/Screenshot 2025-08-25 024536.png', '71', 200, 84, '12 / 07 / 2005', 'Undergraduate', '6723246509', '2415222747304', '0655066971'),
    (358, 30, 'Uma Miller', 'C:/players/team30/Screenshot 2025-08-25 025034.png', 10, 'C:/players/team30/Screenshot 2025-08-25 025034.png', '01', 199, 90, '20 / 09 / 2005', 'Undergraduate', '6627956637', '1302109931367', '0807913745'),
    (359, 30, 'Parker Coleman', 'C:/players/team30/Screenshot 2025-08-25 025037.png', 11, 'C:/players/team30/Screenshot 2025-08-25 025037.png', '87', 189, 61, '24 / 10 / 2004', 'Undergraduate', '6770001622', '1414468374602', '0692355216'),
    (360, 30, 'Caleb Ward', 'C:/players/team30/Screenshot 2025-08-25 025041.png', 12, 'C:/players/team30/Screenshot 2025-08-25 025041.png', '98', 166, 85, '19 / 07 / 2003', 'Undergraduate', '6531707515', '2412805100614', '0875896892'),
    (361, 31, 'Owen Kelly', 'C:/players/team31/Screenshot 2025-09-08 030239.png', 1, 'C:/players/team31/Screenshot 2025-09-08 030239.png', '21', 181, 64, '08 / 01 / 2005', 'Undergraduate', '6511736448', '2464076821915', '0682938526'),
    (362, 31, 'Eli Mehta', 'C:/players/team31/Screenshot 2025-09-08 030241.png', 2, 'C:/players/team31/Screenshot 2025-09-08 030241.png', '08', 170, 71, '12 / 08 / 2005', 'Undergraduate', '6632122207', '1369661872096', '0623201760'),
    (363, 31, 'Finn Rossi', 'C:/players/team31/Screenshot 2025-09-08 030244.png', 3, 'C:/players/team31/Screenshot 2025-09-08 030244.png', '40', 197, 60, '24 / 07 / 2003', 'Undergraduate', '6744383436', '1493703376656', '0657884405'),
    (364, 31, 'Jay Owens', 'C:/players/team31/Screenshot 2025-09-08 030247.png', 4, 'C:/players/team31/Screenshot 2025-09-08 030247.png', '35', 193, 95, '01 / 06 / 2004', 'Undergraduate', '6718203364', '2345291379719', '0634649752'),
    (365, 31, 'Chase Larson', 'C:/players/team31/Screenshot 2025-09-08 030250.png', 5, 'C:/players/team31/Screenshot 2025-09-08 030250.png', '49', 161, 95, '17 / 06 / 2003', 'Undergraduate', '6520439591', '1394334928230', '0919530652'),
    (366, 31, 'June Flores', 'C:/players/team31/Screenshot 2025-09-08 030253.png', 6, 'C:/players/team31/Screenshot 2025-09-08 030253.png', '17', 197, 68, '15 / 03 / 2003', 'Undergraduate', '6609695880', '1321940559028', '0883735664'),
    (367, 31, 'Kara Jordan', 'C:/players/team31/Screenshot 2025-09-08 030256.png', 7, 'C:/players/team31/Screenshot 2025-09-08 030256.png', '85', 175, 65, '12 / 07 / 2003', 'Undergraduate', '6589023149', '2368615972188', '0857399243'),
    (368, 31, 'Zara Wood', 'C:/players/team31/Screenshot 2025-09-08 030259.png', 8, 'C:/players/team31/Screenshot 2025-09-08 030259.png', '39', 157, 97, '30 / 04 / 2004', 'Undergraduate', '6777877066', '1469915401846', '0699529696'),
    (369, 31, 'Casey Vargas', 'C:/players/team31/Screenshot 2025-09-08 030302.png', 9, 'C:/players/team31/Screenshot 2025-09-08 030302.png', '38', 162, 93, '24 / 01 / 2005', 'Undergraduate', '6761956711', '1384667075606', '0614436640'),
    (370, 31, 'Skye Ramirez', 'C:/players/team31/Screenshot 2025-09-08 030305.png', 10, 'C:/players/team31/Screenshot 2025-09-08 030305.png', '34', 181, 93, '04 / 11 / 2004', 'Undergraduate', '6782302366', '1364745045081', '0866715657'),
    (371, 31, 'Jude Ross', 'C:/players/team31/Screenshot 2025-09-08 030312.png', 11, 'C:/players/team31/Screenshot 2025-09-08 030312.png', '25', 193, 95, '06 / 05 / 2004', 'Undergraduate', '6788051117', '1309508942458', '0886783513'),
    (372, 31, 'Piper Ueda', 'C:/players/team31/Screenshot 2025-09-08 030314.png', 12, 'C:/players/team31/Screenshot 2025-09-08 030314.png', '02', 178, 63, '20 / 03 / 2004', 'Undergraduate', '6774518971', '1483451434070', '0679764225'),
    (373, 32, 'Troy Nolan', 'C:/players/team32/Screenshot 2025-09-08 030343.png', 1, 'C:/players/team32/Screenshot 2025-09-08 030343.png', '52', 162, 74, '11 / 02 / 2003', 'Undergraduate', '6791502452', '2439942035195', '0835445815'),
    (374, 32, 'Levi Jones', 'C:/players/team32/Screenshot 2025-09-08 030345.png', 2, 'C:/players/team32/Screenshot 2025-09-08 030345.png', '76', 183, 86, '23 / 02 / 2005', 'Undergraduate', '6503550352', '2343982966985', '0957486794'),
    (375, 32, 'Jasper Hughes', 'C:/players/team32/Screenshot 2025-09-08 030349.png', 3, 'C:/players/team32/Screenshot 2025-09-08 030349.png', '83', 161, 55, '05 / 08 / 2003', 'Undergraduate', '6689798635', '2354725751212', '0697295405'),
    (376, 32, 'Casey Walsh', 'C:/players/team32/Screenshot 2025-09-08 030352.png', 4, 'C:/players/team32/Screenshot 2025-09-08 030352.png', '41', 193, 80, '28 / 03 / 2003', 'Undergraduate', '6753898386', '2309172497096', '0867337275'),
    (377, 32, 'Talon Reed', 'C:/players/team32/Screenshot 2025-09-08 030355.png', 5, 'C:/players/team32/Screenshot 2025-09-08 030355.png', '34', 179, 84, '26 / 08 / 2004', 'Undergraduate', '6625954363', '2363549625433', '0823960009'),
    (378, 32, 'Faith Wilson', 'C:/players/team32/Screenshot 2025-09-08 030357.png', 6, 'C:/players/team32/Screenshot 2025-09-08 030357.png', '37', 186, 58, '13 / 09 / 2003', 'Undergraduate', '6533778368', '1498748879538', '0690149164'),
    (379, 32, 'Finn Evans', 'C:/players/team32/Screenshot 2025-09-08 030400.png', 7, 'C:/players/team32/Screenshot 2025-09-08 030400.png', '25', 170, 67, '17 / 09 / 2003', 'Undergraduate', '6588939653', '1352416697604', '0662062042'),
    (380, 32, 'Derek Kelly', 'C:/players/team32/Screenshot 2025-09-08 030403.png', 8, 'C:/players/team32/Screenshot 2025-09-08 030403.png', '88', 155, 86, '04 / 06 / 2003', 'Undergraduate', '6687426802', '1456384581960', '0860045318'),
    (381, 32, 'Levi Foster', 'C:/players/team32/Screenshot 2025-09-08 030405.png', 9, 'C:/players/team32/Screenshot 2025-09-08 030405.png', '44', 194, 54, '05 / 04 / 2005', 'Undergraduate', '6794620230', '1384307907146', '0608417429'),
    (382, 32, 'Felix Zimmerman', 'C:/players/team32/Screenshot 2025-09-08 030408.png', 10, 'C:/players/team32/Screenshot 2025-09-08 030408.png', '75', 170, 68, '21 / 06 / 2005', 'Undergraduate', '6638739573', '2342801547879', '0925917328'),
    (383, 32, 'Colin Wong', 'C:/players/team32/Screenshot 2025-09-08 030411.png', 11, 'C:/players/team32/Screenshot 2025-09-08 030411.png', '48', 157, 72, '27 / 05 / 2004', 'Undergraduate', '6722691643', '2451737238902', '0986117764'),
    (384, 32, 'Avery Hughes', 'C:/players/team32/Screenshot 2025-09-08 030415.png', 12, 'C:/players/team32/Screenshot 2025-09-08 030415.png', '81', 181, 68, '10 / 02 / 2004', 'Undergraduate', '6744056053', '1376766970184', '0811529667');

    """)
    connection.commit()
    connection.close()

def del_team_navyy():
    import sqlite3

    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()
    # cursor.execute('''DELETE FROM players;''')
    cursor.execute('''DELETE FROM matches;''')
    cursor.execute('''DELETE FROM fouls;''')
    cursor.execute('''DELETE FROM scores;''')
    cursor.execute('''DELETE FROM substitutions;''')
    cursor.execute('''DELETE FROM timeouts;''')
    # cursor.execute('''DELETE FROM teams WHERE username = 'navyy';''')
    connection.commit()
    connection.close()

def insert_team_navyy():
    import sqlite3

    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO teams (team_id, username, team_name, tournament_name)
    VALUES
    (1,  'navyy', 'kku1',  'KKU GAME'),
    (2,  'navyy', 'kku2',  'KKU GAME'),
    (3,  'navyy', 'kku3',  'KKU GAME'),
    (4,  'navyy', 'kku4',  'KKU GAME'),
    (5,  'navyy', 'kku5',  'KKU GAME'),
    (6,  'navyy', 'kku6',  'KKU GAME'),
    (7,  'navyy', 'kku7',  'KKU GAME'),
    (8,  'navyy', 'kku8',  'KKU GAME'),
    (9,  'navyy', 'kku9',  'KKU GAME'),
    (10, 'navyy', 'kku10', 'KKU GAME'),
    (11, 'navyy', 'kku11', 'KKU GAME'),
    (12, 'navyy', 'kku12', 'KKU GAME'),
    (13, 'navyy', 'kku13', 'KKU GAME'),
    (14, 'navyy', 'kku14', 'KKU GAME'),
    (15, 'navyy', 'kku15', 'KKU GAME'),
    (16, 'navyy', 'kku16', 'KKU GAME'),
    (17, 'navyy', 'kku17', 'KKU GAME'),
    (18, 'navyy', 'kku18', 'KKU GAME'),
    (19, 'navyy', 'kku19', 'KKU GAME'),
    (20, 'navyy', 'kku20', 'KKU GAME'),
    (21, 'navyy', 'kku21', 'KKU GAME'),
    (22, 'navyy', 'kku22', 'KKU GAME'),
    (23, 'navyy', 'kku23', 'KKU GAME'),
    (24, 'navyy', 'kku24', 'KKU GAME'),
    (25, 'navyy', 'kku25', 'KKU GAME'),
    (26, 'navyy', 'kku26', 'KKU GAME'),
    (27, 'navyy', 'kku27', 'KKU GAME'),
    (28, 'navyy', 'kku28', 'KKU GAME'),
    (29, 'navyy', 'kku29', 'KKU GAME'),
    (30, 'navyy', 'kku30', 'KKU GAME'),
    (31, 'navyy', 'kku31', 'KKU GAME'),
    (32, 'navyy', 'kku32', 'KKU GAME');''')
    connection.commit()
    connection.close()

def create_database_2():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS user_account (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NULL CHECK(length(username) BETWEEN 5 AND 30),
            password TEXT NULL CHECK(length(password) BETWEEN 8 AND 20),
            fullname TEXT NULL CHECK(length(fullname) <= 747),
            phone_number TEXT NULL CHECK(length(phone_number) = 10),
            email TEXT NULL UNIQUE CHECK(
                (email LIKE '%@gmail.com' OR
                email LIKE '%@outlook.com' OR
                email LIKE '%@yahoo.com' OR
                email LIKE '%@icloud.com' OR
                email LIKE '%@hotmail.com' OR
                email LIKE '%@kkumail.com')
                AND length(email) BETWEEN 6 AND 30
            )
        );
    '''
    cursor.execute(create_table_query)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            username TEXT NOT NULL,
            tournament_name TEXT NOT NULL,
            FOREIGN KEY(username) REFERENCES user_account(username)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            team_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            team_name TEXT NOT NULL,
            tournament_name TEXT NOT NULL,
            FOREIGN KEY(username) REFERENCES user_account(username)
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                player_id INTEGER PRIMARY KEY AUTOINCREMENT,
                team_id INTEGER NOT NULL,
                player_name TEXT NOT NULL,
                player_image_path TEXT,
                button_id INTEGER NOT NULL,
                button_object_name TEXT NOT NULL,
                player_number TEXT,
                player_height TEXT,
                player_weight TEXT,
                player_birthday TEXT,
                player_status TEXT,
                student_id TEXT,
                thai_id TEXT,
                phone_number TEXT,
                FOREIGN KEY(team_id) REFERENCES teams(team_id)
            )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS layouts (
            layout_id INTEGER PRIMARY KEY AUTOINCREMENT,
            team_id INTEGER NOT NULL,
            layout_name TEXT NOT NULL,
            layout_exists INTEGER NOT NULL CHECK (layout_exists IN (0, 1)),
            FOREIGN KEY(team_id) REFERENCES teams(team_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS spacers (
            spacer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            layout_id INTEGER NOT NULL,
            index_position INTEGER NOT NULL,
            width INTEGER NOT NULL,
            height INTEGER NOT NULL,
            FOREIGN KEY(layout_id) REFERENCES layouts(layout_id)
        )
    ''')
    connection.commit()
    connection.close()
    print("Database created successfully!")

def create_database_for_match_result():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()

    # ตารางการแข่งขัน
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS matches (
        match_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        match_date TEXT NOT NULL,
        team1_id INTEGER NOT NULL,
        team2_id INTEGER NOT NULL,
        winner TEXT
    )""")

    # ตารางผู้เล่น
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        team_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        number INTEGER NOT NULL,
        is_starter BOOLEAN NOT NULL
    )""")

    # ตารางการเปลี่ยนตัว
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS substitutions (
            sub_id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_id INTEGER NOT NULL,
            team_id INTEGER NOT NULL,
            player_out INTEGER NOT NULL,
            player_in INTEGER NOT NULL,
            time TEXT NOT NULL,
            period INTEGER NOT NULL
        )""")

    # ตารางฟาวล์
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fouls (
        foul_id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INTEGER NOT NULL,
        player_id INTEGER NOT NULL,
        time TEXT NOT NULL,
        period INTEGER NOT NULL
    )""")

    # ตารางการขอเวลานอก
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS timeouts (
        timeout_id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INTEGER NOT NULL,
        team_id INTEGER NOT NULL,
        time TEXT NOT NULL,
        period INTEGER NOT NULL
    )""")

    # ตารางคะแนนแต่ละ period
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INTEGER NOT NULL,
        period INTEGER NOT NULL,
        team1_score INTEGER NOT NULL,
        team2_score INTEGER NOT NULL,
        period_winner TEXT NOT NULL
    )""")

    connection.commit()
    connection.close()

def create_database_for_match_result1():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()

    # ตารางการแข่งขัน
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS matches (
        match_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        match_date TEXT NOT NULL,
        team1_id INTEGER NOT NULL,
        team2_id INTEGER NOT NULL,
        winner TEXT
    )""")

    # ตารางผู้เล่น
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        player_id INTEGER PRIMARY KEY AUTOINCREMENT,
        team_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        number INTEGER NOT NULL,
        is_starter BOOLEAN NOT NULL
    )""")

    # ตารางการเปลี่ยนตัว
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS substitutions (
            sub_id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_id INTEGER NOT NULL,
            team_id INTEGER NOT NULL,
            player_out INTEGER NOT NULL,
            player_in INTEGER NOT NULL,
            time TEXT NOT NULL,
            period INTEGER NOT NULL
        )""")

    # ตารางฟาวล์
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fouls (
        foul_id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INTEGER NOT NULL,
        team TEXT NOT NULL,
        player_id INTEGER NOT NULL,
        time TEXT NOT NULL,
        period INTEGER NOT NULL
    )""")

    # ตารางการขอเวลานอก
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS timeouts (
        timeout_id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INTEGER NOT NULL,
        team_id INTEGER NOT NULL,
        time TEXT NOT NULL,
        period INTEGER NOT NULL
    )""")

    # ตารางคะแนนแต่ละ period
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        match_id INTEGER NOT NULL,
        period INTEGER NOT NULL,
        team1_score INTEGER NOT NULL,
        team2_score INTEGER NOT NULL,
        period_winner TEXT NOT NULL
    )""")

    connection.commit()
    connection.close()

def del_db_1():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM user_account')
    connection.commit()
    connection.close()
    print("user_account deleted successfully!")

def del_db_2():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM teams')
    cursor.execute('DELETE FROM players')
    connection.commit()
    connection.close()
    print("teams, players, layouts, spacers deleted successfully!")

def del_matches():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM matches')
    cursor.execute('DELETE FROM substitutions')
    cursor.execute('DELETE FROM fouls')
    cursor.execute('DELETE FROM timeouts')
    cursor.execute('DELETE FROM scores')
    connection.commit()
    connection.close()
    print("matches deleted successfully!")

def clear_all_except_user_account():
    connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
    cursor = connection.cursor()
    # ลบข้อมูลในทุกตารางที่ไม่ใช่ user_account
    cursor.execute('DELETE FROM teams')
    cursor.execute('DELETE FROM players')
    cursor.execute('DELETE FROM matches')
    cursor.execute('DELETE FROM substitutions')
    cursor.execute('DELETE FROM fouls')
    cursor.execute('DELETE FROM timeouts')
    cursor.execute('DELETE FROM scores')
    cursor.execute('DELETE FROM tournament')
    connection.commit()
    connection.close()
    print("Cleared all data except user_account.")

# clear_all_except_user_account()
# insert_players()
del_team_navyy()
