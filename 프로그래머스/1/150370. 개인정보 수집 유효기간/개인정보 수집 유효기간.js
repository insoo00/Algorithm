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
        
        
        let tmpM = dateM+termsInfo[t];
        if(tmpM>12) {
            dateY = tmpM%12===0 ? dateY+(parseInt(tmpM/12))-1 : dateY+(parseInt(tmpM/12))
            dateM = tmpM%12===0 ? 12 : tmpM%12
        } else {
            dateM = tmpM
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