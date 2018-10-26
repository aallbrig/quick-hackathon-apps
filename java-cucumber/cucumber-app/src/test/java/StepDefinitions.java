import cucumber.api.PendingException;
import cucumber.api.java.After;
import cucumber.api.java.Before;
import cucumber.api.java.en.*;
import com.aallbright.App;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;

public class StepDefinitions {
    private App app;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final ByteArrayOutputStream errContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;
    private final PrintStream originalErr = System.err;

    @Given("^I have an app$")
    public void i_have_an_app() throws Throwable {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
        App.main(new String[]{});
    }

    @Then("^I see hello world$")
    public void i_see_hello_world() throws Throwable {
        assertEquals("Hello World!\n", outContent.toString());
    }

}
