function solution(s) {
    let tempS = '';
    const answer = [];
    for (let i = 0; i < s.length; i++) {
        if (tempS.includes(s[i])) {
            answer.push(i - tempS.lastIndexOf(s[i]));
        } else {
            answer.push(-1);
        }
        tempS = tempS + s[i];
    }
    return answer;
}