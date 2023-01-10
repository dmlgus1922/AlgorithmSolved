function solution(A, B) {
    const len = A.length;
    let temp = A;
    for (let i = 0; i < len; i++) {
        if (temp === B) {
            return i;
        }
        temp = temp.slice(len-1) + temp.slice(0, len-1);
    }
    return -1;
}