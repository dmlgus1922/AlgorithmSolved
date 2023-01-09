function solution(num, total) {
    const mid = Math.floor(total/num);
    const start = Math.floor(num/2);
    if (num % 2 == 1) {
        return [...Array(num).keys()].map(key => key + (mid - start));
    } else {
        return [...Array(num).keys()].map(key => key + (mid - start + 1));
    }
}