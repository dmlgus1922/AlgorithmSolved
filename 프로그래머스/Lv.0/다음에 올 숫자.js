function solution(common) {
    const l = common.length
    let [a, b, c] = [common[l-1], common[l-2], common[l-3]];
    if (a - b === b - c) {
        return a + (a - b)
    } else {
        return a * (a / b)
    }
}