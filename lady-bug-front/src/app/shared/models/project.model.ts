export class Project {
    constructor(
        public name?: string,
        public client?: string,
        public description?: string,
        public team?: string[],

        public testSuitename?: string,
        public testSuiteDescription?: string,
        public testSuiteInportance?: string,
        public testesCases?: string[],
        public testSuiteSteps?: string,
        public testSuitePreConditions?: string,
    ){}
}