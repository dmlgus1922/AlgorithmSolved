function solution(k, score) {
    const answer = [];
    for (let i = 1; i <= score.length; i++) {
        const sortedScore = score.slice(0, i).sort((a,b) => {return b-a});
        answer.push(sortedScore.slice(0, k)[i < k ? i-1 : k-1]);
    }
    return answer;
}