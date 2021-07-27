export class Bug {
    constructor(
        public testSuitename?: string,
        public testesCases?: string[],
        public developer?: string,
        public observations?: string,
    ){}
}