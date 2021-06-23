const present = new Date();
let weekDay = present.getDay();
let date = present.getDate();
let month = present.getMonth() + 1;
let year = present.getFullYear();

let standard = [["mon1", "Phòng 2", "June 28, 2021", "July 4, 2021", "MWF"], ["mon1", "Phòng 2", "June 21, 2021", "June 27, 2021", "MWF"], ["mon1", "Phòng 2", "June 14, 2021", "June 20, 2021", "MWF"], ["mon2", "Phòng 2", "July 19, 2021", "July 25, 2021", "MWF"], ["mon2", "Phòng 2", "July 12, 2021", "July 18, 2021", "MWF"], ["mon2", "Phòng 2", "July 5, 2021", "July 11, 2021", "MWF"], ["Frontend advance 1", "Phòng 2", "Aug. 16, 2021", "Aug. 22, 2021", "MWF"], ["Frontend advance 1", "Phòng 2", "Aug. 9, 2021", "Aug. 15, 2021", "MWF"], ["Frontend advance 1", "Phòng 2", "Aug. 2, 2021", "Aug. 8, 2021", "MWF"], ["Frontend advance 1", "Phòng 2", "July 26, 2021", "Aug. 1, 2021", "MWF"], ["new", "Phòng 3", "July 5, 2021", "July 11, 2021", "MWF"], ["new", "Phòng 3", "June 28, 2021", "July 4, 2021", "MWF"], ["new", "Phòng 3", "June 21, 2021", "June 27, 2021", "MWF"], ["new", "Phòng 3", "June 14, 2021", "June 20, 2021", "MWF"], ["Backend Basic 2", "Phòng 3", "Aug. 16, 2021", "Aug. 22, 2021", "MWF"], ["Backend Basic 2", "Phòng 3", "Aug. 9, 2021", "Aug. 15, 2021", "MWF"], ["Backend Basic 2", "Phòng 3", "Aug. 2, 2021", "Aug. 8, 2021", "MWF"], ["Backend Basic 2", "Phòng 3", "July 26, 2021", "Aug. 1, 2021", "MWF"], ["Backend Basic 2", "Phòng 3", "July 19, 2021", "July 25, 2021", "MWF"], ["Backend Basic 2", "Phòng 3", "July 12, 2021", "July 18, 2021", "MWF"], ["Frontend basic 1", "Phòng 1", "June 28, 2021", "July 4, 2021", "TTS"], ["Frontend basic 1", "Phòng 1", "June 21, 2021", "June 27, 2021", "TTS"], ["Frontend basic 1", "Phòng 1", "June 14, 2021", "June 20, 2021", "TTS"], ["ádasd", "Phòng 1", "July 19, 2021", "July 25, 2021", "TTS"], ["ádasd", "Phòng 1", "July 12, 2021", "July 18, 2021", "TTS"], ["ádasd", "Phòng 1", "July 5, 2021", "July 11, 2021", "TTS"], ["mon5", "Phòng 3", "June 28, 2021", "July 4, 2021", "TTS"], ["mon5", "Phòng 3", "June 21, 2021", "June 27, 2021", "TTS"], ["mon5", "Phòng 3", "June 14, 2021", "June 20, 2021", "TTS"], ["mon3", "Phòng 2", "July 5, 2021", "July 11, 2021", "TTS"], ["mon3", "Phòng 2", "June 28, 2021", "July 4, 2021", "TTS"], ["mon3", "Phòng 2", "June 21, 2021", "June 27, 2021", "TTS"], ["mon3", "Phòng 2", "June 14, 2021", "June 20, 2021", "TTS"], ["Backend Basic 1", "Phòng 3", "Aug. 9, 2021", "Aug. 15, 2021", "TTS"], ["Backend Basic 1", "Phòng 3", "Aug. 2, 2021", "Aug. 8, 2021", "TTS"], ["Backend Basic 1", "Phòng 3", "July 26, 2021", "Aug. 1, 2021", "TTS"], ["Backend Basic 1", "Phòng 3", "July 19, 2021", "July 25, 2021", "TTS"], ["Backend Basic 1", "Phòng 3", "July 12, 2021", "July 18, 2021", "TTS"], ["Backend Basic 1", "Phòng 3", "July 5, 2021", "July 11, 2021", "TTS"]]

getNow();
checkSameWeek();

$(".pre").click(function () {
    for (let i = 0; i < 7; i++) {
        $(`.week-names > .${i} > p`).remove();
    }

    $(`.abc > p`).remove();

    dateSubtraction();
    checkSameWeek();

});

$(".now").click(function () {
    for (let i = 0; i < 7; i++) {
        $(`.week-names > .${i} > p`).remove();
    }

    $(`.abc > p`).remove();

    getNow();
    checkSameWeek();
});

$(".next").click(function () {
    for (let i = 0; i < 7; i++) {
        $(`.week-names > .${i} > p`).remove();
    }

    $(`.abc > p`).remove();

    dateAddition();

    checkSameWeek();
});

function dateSubtraction() {
    if (date <= 14) {
        if (month >= 2 && month <= 12) {
            month -= 1;

            if (
                (month === 1 ||
                    month === 3 ||
                    month === 5 ||
                    month === 7 ||
                    month === 8 ||
                    month === 10) &&
                month !== 12
            ) {
                date = 17 + date;
            } else {
                if (month === 2) {
                    if (year % 4 === 0 && year % 100 !== 0) {
                        date = 15 + date;
                    } else {
                        date = 14 + date;
                    }
                } else {
                    date = 16 + date;
                }
            }
        } else {
            month = 12;
            year -= 1;
            date = 17 + date;
        }
    } else {
        date -= 14;
    }

    dateAddition();
}

function getNow() {
    weekDay = present.getDay();
    date = present.getDate();
    month = present.getMonth() + 1;
    year = present.getFullYear();

    if (date > 7) {
        switch (weekDay) {
            case 0:
                date -= 7;
                break;
            case 1:
                date -= 1;
                break;
            case 2:
                date -= 2;
                break;
            case 3:
                date -= 3;
                break;
            case 4:
                date -= 4;
                break;
            case 5:
                date -= 5;
                break;
            case 6:
                date = weekDate - 6;
                break;
        }
    } else {
        switch (weekDay) {
            case 0:
                if (
                    month === 1 ||
                    month === 2 ||
                    month === 4 ||
                    month === 6 ||
                    month === 9 ||
                    month === 11
                ) {
                    month -= 1;
                    date += 24;
                } else {
                    if (month === 5 || month === 7 || month === 10 || month === 12) {
                        date += 23;
                        month -= 1;
                    } else {
                        if (month === 3) {
                            if ((year % 4 === 0 && year % 100 !== 0) || year % 400 == 0) {
                                date += 22;
                                month -= 1;
                            } else {
                                date += 21;
                                month -= 1;
                            }
                        }
                    }
                }

                break;
            case 1:
                if (date > 1) {
                    date -= 1;
                } else {
                    if (
                        month === 1 ||
                        month === 2 ||
                        month === 4 ||
                        month === 6 ||
                        month === 9 ||
                        month === 11
                    ) {
                        date = 31;
                        month -= 1;
                    } else {
                        if (month === 5 || month === 7 || month === 10 || month === 12) {
                            date = 30;
                            month -= 1;
                        } else {
                            if (month === 3) {
                                if ((year % 4 === 0 && year % 100 !== 0) || year % 400 == 0) {
                                    date += 22;
                                    month -= 1;
                                } else {
                                    month -= 1;
                                    date += 21;
                                }
                            }
                        }
                    }
                }

                break;
            case 2:
                if (date > 2) {
                    date -= 2;
                } else {
                    if (
                        month === 1 ||
                        month === 2 ||
                        month === 4 ||
                        month === 6 ||
                        month === 9 ||
                        month === 11
                    ) {
                        date += 29;
                        month -= 1;
                    } else {
                        if (month === 5 || month === 7 || month === 10 || month === 12) {
                            date += 28;
                            month -= 1;
                        } else {
                            if (month === 3) {
                                if ((year % 4 === 0 && year % 100 !== 0) || year % 400 == 0) {
                                    date += 27;
                                    month -= 1;
                                } else {
                                    month -= 1;
                                    date += 26;
                                }
                            }
                        }
                    }
                }
                break;
            case 3:
                if (date > 3) {
                    date -= 3;
                } else {
                    if (
                        month === 1 ||
                        month === 2 ||
                        month === 4 ||
                        month === 6 ||
                        month === 9 ||
                        month === 11
                    ) {
                        date += 28;
                        month -= 1;
                    } else {
                        if (month === 5 || month === 7 || month === 10 || month === 12) {
                            date += 27;
                            month -= 1;
                        } else {
                            if (month === 3) {
                                if ((year % 4 === 0 && year % 100 !== 0) || year % 400 == 0) {
                                    date += 26;
                                    month -= 1;
                                } else {
                                    month -= 1;
                                    date += 25;
                                }
                            }
                        }
                    }
                }
                break;
            case 4:
                if (date > 4) {
                    date -= 4;
                } else {
                    if (
                        month === 1 ||
                        month === 2 ||
                        month === 4 ||
                        month === 6 ||
                        month === 9 ||
                        month === 11
                    ) {
                        date += 27;
                        month -= 1;
                    } else {
                        if (month === 5 || month === 7 || month === 10 || month === 12) {
                            date += 26;
                            month -= 1;
                        } else {
                            if (month === 3) {
                                if ((year % 4 === 0 && year % 100 !== 0) || year % 400 == 0) {
                                    date += 25;
                                    month -= 1;
                                } else {
                                    month -= 1;
                                    date += 24;
                                }
                            }
                        }
                    }
                }
                break;
            case 5:
                if (date > 5) {
                    date -= 5;
                } else {
                    if (
                        month === 1 ||
                        month === 2 ||
                        month === 4 ||
                        month === 6 ||
                        month === 9 ||
                        month === 11
                    ) {
                        date += 26;
                        month -= 1;
                    } else {
                        if (month === 5 || month === 7 || month === 10 || month === 12) {
                            date += 25;
                            month -= 1;
                        } else {
                            if (month === 3) {
                                if ((year % 4 === 0 && year % 100 !== 0) || year % 400 == 0) {
                                    date += 24;
                                    month -= 1;
                                } else {
                                    month -= 1;
                                    date += 23;
                                }
                            }
                        }
                    }
                }
                break;
            case 6:
                if (date > 6) {
                    date -= 6;
                } else {
                    if (
                        month === 1 ||
                        month === 2 ||
                        month === 4 ||
                        month === 6 ||
                        month === 9 ||
                        month === 11
                    ) {
                        date += 25;
                        month -= 1;
                    } else {
                        if (month === 5 || month === 7 || month === 10 || month === 12) {
                            date += 24;
                            month -= 1;
                        } else {
                            if (month === 3) {
                                if ((year % 4 === 0 && year % 100 !== 0) || year % 400 == 0) {
                                    date += 23;
                                    month -= 1;
                                } else {
                                    month -= 1;
                                    date += 22;
                                }
                            }
                        }
                    }
                }
                break;
        }
    }

    dateAddition();
}

function dateAddition() {
    for (let i = 0; i < 7; i++) {
        date += 1;
        if (
            ((month === 1 ||
                month === 3 ||
                month === 5 ||
                month === 7 ||
                month === 8 ||
                month === 10) &&
                date > 31) ||
            ((month === 4 || month === 6 || month === 9 || month === 11) &&
                date > 30) ||
            (month === 2 &&
                ((year % 4 === 0 && year % 100 !== 0) || year % 400 == 0) &&
                date > 29) ||
            (month === 2 &&
                !((year % 4 === 0 && year % 100 !== 0) || year % 400 == 0) &&
                date > 28)
        ) {
            date = 1;
            month += 1;
        } else {
            if (month === 12 && date > 31) {
                date = 1;
                month = 1;
                year += 1;
            }
        }

        $(`.week-names > .${i}`).append(`<p>${date}/${month}/${year}<p/>`);
    }
}

function checkSameWeek() {
    let currentSunday = new Date(`${month}/${date}/${year}`);
    for (let i = 0; i < standard.length; i++) {
        let sD = new Date(standard[i][2]);
        if (currentSunday - sD === 518400000) {
            let schedule = standard[i][4];

            switch (schedule) {
                case "MWF":
                    $(`.day_1.full_${standard[i][1][6]}`).append(`<p>${standard[i][0]}<p/>`);

                    $(`.day_3.full_${standard[i][1][6]}`).append(`<p>${standard[i][0]}<p/>`);

                    $(`.day_5.full_${standard[i][1][6]}`).append(`<p>${standard[i][0]}<p/>`);

                    $(`.abc > p:nth-child(2)`).remove();
                    break;

                case "TTS":
                    $(`.day_2.full_${standard[i][1][6]}`).append(`<p>${standard[i][0]}<p/>`);

                    $(`.day_4.full_${standard[i][1][6]}`).append(`<p>${standard[i][0]}<p/>`);

                    $(`.day_6.full_${standard[i][1][6]}`).append(`<p>${standard[i][0]}<p/>`);

                    $(`.abc > p:nth-child(2)`).remove();
                    break;
            }
        }
    }
}