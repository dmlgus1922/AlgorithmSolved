function solution(t, p) {
    const tLen = t.length;
    const pLen = p.length;
    const pNum = parseInt(p);
    const nums = [];
    for (let i = 0; i < tLen - pLen + 1; i ++) {
        const num = t.slice(i, i+pLen);
        nums.push(parseInt(num));
    }
    const answer = nums.filter(num => {return num <= pNum});
    return answer.length;
}