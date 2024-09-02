function solution(today, terms, privacies) {
    var answer = [];
    
    const [todayY, todayM, todayD] = today.split(".").map(Number);
    const termsInfo = {};
    for (let term of terms) {
        const [type, month] = term.split(" ");
        termsInfo[type] = Number(month);
    }
    
    let idx = 1;
    for (let privacy of privacies) {
        let [date, t] = privacy.split(" ");
        let [dateY, dateM, dateD] = date.split(".").map(Number);
        
        // dateM += termsInfo[t];
        // if (dateM > 12) {
        //     dateY += 1;
        //     dateM -= 12;
        // }
        
        const checkDate=(year, month, exp)=>{
            const testMonth=exp+month;
            let newYear=testMonth%12===0 ? year+(parseInt(testMonth/12))-1 : year+(parseInt(testMonth/12))
            let newMonth=testMonth%12===0 ? 12 : testMonth%12

            return {'year': newYear,'month':newMonth}
        }
        
        if(dateM+termsInfo[t]>12) {
            dateY = checkDate(dateY, dateM, termsInfo[t]).year
            dateM = checkDate(dateY, dateM, termsInfo[t]).month
        } else {
            dateM = dateM+termsInfo[t]
        }


        
        if (todayY > dateY) {
            answer.push(idx);
        }
        else if (todayY === dateY) {
            if(todayM > dateM) {
                answer.push(idx);
            } else if (todayM === dateM) {
                if (todayD >= dateD) {
                    answer.push(idx);
                }
            }
        }
        
        idx++;    
    }
    
    
    return answer;
}