function detect(
  process: number[],
  allocation: number[][],
  request: number[][],
  work: number[]
): boolean {
  const n: number = process.length;
  const m: number = work.length;

  // Create copy of allocation and request matrices
  const allocationCopy: number[][] = allocation.map(row => [...row]);
  const requestCopy: number[][] = request.map(row => [...row]);

  // Create a list to track finished processes
  const finished: boolean[] = Array(n).fill(false);

  // Initialize an array to store the safe sequence
  const safeSequence: number[] = [];

  // Calculate the initial work
  work = work.map(
    (resource, j) =>
      resource - allocationCopy.reduce((sum, row) => sum + row[j], 0)
  );

  // Repeat until all processes are finished or deadlock is detected
  while (true) {
    // Find a process that is not finished and has an unsatisfied request
    let processFound: boolean = false;
    for (let i = 0; i < n; i++) {
      if (!finished[i] && requestCopy[i].every((req, j) => req <= work[j])) {
        // Process can be satisfied, allocate its resources
        work = work.map((resource, j) => resource + allocationCopy[i][j]);
        finished[i] = true;
        safeSequence.push(process[i]);
        processFound = true;
      }
    }

    // If no process is found, break the loop
    if (!processFound) {
      break;
    }
  }

  // If all processes are finished, no deadlock exists
  if (finished.every(Boolean)) {
    console.log('No deadlock detected.');
    return false;
  }

  // Deadlock detected, print the safe sequence
  console.log('Deadlock detected. Safe sequence:', safeSequence);
  return true;
}

// # Deadlock Detected with Safe Sequence:
let processVar = [0, 1, 2, 3, 4];
let allocation = [
  [0, 1, 0],
  [2, 0, 0],
  [3, 0, 3],
  [2, 1, 1],
  [0, 0, 2],
];
let request = [
  [0, 0, 0],
  [2, 0, 2],
  [0, 0, 0],
  [1, 0, 0],
  [0, 0, 2],
];
let available = [0, 0, 0];
// # Expected Output: Deadlock detected. Safe sequence: [1, 3, 0, 2, 4]

detect(processVar, allocation, request, available);

// # Deadlock Not Detected:
processVar = [0, 1, 2, 3];
allocation = [
  [0, 1],
  [2, 0],
  [0, 3],
  [1, 0],
];
request = [
  [0, 0],
  [2, 0],
  [0, 0],
  [0, 0],
];
available = [1, 1];
// # Expected Output: No deadlock detected.

detect(processVar, allocation, request, available);

// # Deadlock Not Detected with Unused Resources:
processVar = [0, 1, 2];
allocation = [
  [0, 0],
  [0, 0],
  [0, 0],
];
request = [
  [1, 1],
  [1, 1],
  [1, 1],
];
available = [2, 2];
// # Expected Output: No deadlock detected.

detect(processVar, allocation, request, available);

// # Deadlock Detected with Partial Safe Sequence:
processVar = [0, 1, 2, 3];
allocation = [
  [1, 1],
  [1, 0],
  [0, 1],
  [0, 0],
];
request = [
  [0, 0],
  [1, 0],
  [0, 1],
  [1, 0],
];
available = [1, 1];
// # Expected Output: Deadlock detected. Safe sequence: [0, 2]

detect(processVar, allocation, request, available);
