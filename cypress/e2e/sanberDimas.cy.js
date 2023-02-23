describe("Register Page Test Cases", () => {

    it("Login with correct values", () => {
        //Login Using Correct Username & Password
        cy.visit("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
        const usernm = cy.get("input[name='username']");
        usernm.type("Admin");
        const pass = cy.get("input[name='password']");
        pass.type("admin123");

        const btn = cy.get(".oxd-button");
        btn.click();
        cy.wait(2000)

        const ddBtn = cy.get('.oxd-userdropdown-tab')
        ddBtn.click();

        cy.wait(2500)
        const logbtn = cy.get(':nth-child(4) > .oxd-userdropdown-link');
        logbtn.click();      

    });

    it("Login with correct Username & Wrong Password", () => {
        //Login Using Correct Username & Wrong Password
        cy.visit("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
        const usernm = cy.get("input[name='username']");
        usernm.type("Admin");
        const pass = cy.get("input[name='password']");
        pass.type("aaaa");

        const btn = cy.get(".oxd-button");
        btn.click();
        cy.wait(2000)

    });

    it("//Login Using inCorrect Username & Correct Password", () => {
        //Login Using inCorrect Username & Correct Password
        cy.visit("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
        const usernm = cy.get("input[name='username']");
        usernm.type("bangGober");
        const pass = cy.get("input[name='password']");
        pass.type("admin123");

        const btn = cy.get(".oxd-button");
        btn.click();
        cy.wait(2000)

    });

    it("//Login Using Null Username & Null Password", () => {
        //Login Using null Username & null Password
        cy.visit("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
        const usernm = cy.get("input[name='username']");
        usernm.type(" ");
        const pass = cy.get("input[name='password']");
        pass.type(" ");

        const btn = cy.get(".oxd-button");
        btn.click();
        cy.wait(2000)

    });

    it("//Login Using inCorrect Username & InCorrect Password", () => {
        //Login Using inCorrect Username & inCorrect Password
        cy.visit("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
        const usernm = cy.get("input[name='username']");
        usernm.type("dgjasdahj");
        const pass = cy.get("input[name='password']");
        pass.type("taatat");

        const btn = cy.get(".oxd-button");
        btn.click();
        cy.wait(2000)

    });

});
