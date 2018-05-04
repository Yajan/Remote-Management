import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import java.io.File;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import org.apache.commons.cli.*;
import java.util.TimeZone;


public class XMLParser {
    public static void main(String[] args) {
//        String dtime = militime("2018:04:25:20:29:00");
//        editJMX("C:\\Users\\Yajana\\Downloads\\scale_up_infra-master\\scale_up_infra-master\\Scripts\\Chrome\\SanityFileupload.jmx",dtime);


        Options options = new Options();

        Option action = new Option("action",true,"Action");
        options.addOption(action);

        Option script = new Option("script",true,"JMX Script");
        options.addOption(script);

        Option url = new Option("url",true,"HTTP request");
        options.addOption(url);

        Option count = new Option("count",true,"Iteration");
        options.addOption(count);

        Option thread = new Option("thread",true,"Number of Users");
        options.addOption(thread);

        Option rampup = new Option("rampup",true,"Rampup In Seconds");
        options.addOption(rampup);


        Option timer = new Option("t","timer",true,"Start Time in yyyy:MM:dd:hh:mm:ss");
        options.addOption(timer);

        CommandLineParser parser = new DefaultParser();
        HelpFormatter formatter = new HelpFormatter();
        CommandLine cmd;

        try{
            cmd = parser.parse(options,args);
        }catch (ParseException e){
            System.out.println(e.getMessage());
            formatter.printHelp("jmeter_editor",options);

            System.exit(1);
            return;
        }
        String act = cmd.getOptionValue("action");
        if (act == null){
            formatter.printHelp("jmeter_editor",options);
            System.out.println("No action is given perfrom");
            System.out.println("Existing the program");
            System.exit(1);
            return;

        }
        if(act.equalsIgnoreCase("create")){
            if( cmd.getOptionValue("thread") != null && cmd.getOptionValue("count") != null || cmd.getOptionValue("rampup") != null) {
                System.out.println("Execution started @ "+logTime());
                Create.createJMX(cmd.getOptionValue("url"), cmd.getOptionValue("thread"), cmd.getOptionValue("count"), cmd.getOptionValue("rampup"));
                System.out.println("Executoin completed @"+logTime());
            }
            else {
                System.out.println("Execution started @ "+logTime());
                Create.createJMX(cmd.getOptionValue("url"));
                System.out.println("Completed @ "+logTime());
            }
        }
        else if (act.equalsIgnoreCase("edit")){
            String filename = cmd.getOptionValue("script");
            String stime = cmd.getOptionValue("timer");
            System.out.println("JMX Editing started @ "+logTime());

            System.out.println("JMX script to edit : "+filename);
            System.out.println("Time to start the test : "+stime);
            String time = militime(stime);
            System.out.println("Time in mili seconds : "+time);
            Edit.editJMX(filename,time);
            System.out.println("JMX Editing completed @ :"+logTime());
        }



    }

    public static String militime(String time) {
        try {
            DateFormat sdf = new SimpleDateFormat("yyyy:MM:dd:hh:mm:ss");

            Date date = sdf.parse(time);

            Calendar now = Calendar.getInstance();
            TimeZone timeZone = now.getTimeZone();
            System.out.println("Current Timezone is : "+timeZone.getDisplayName());

            sdf.setTimeZone(timeZone);

            String militime = String.valueOf(date.getTime());
//            System.out.println(militime);
            return militime;
        }catch (Exception  exec){
            return String.valueOf(exec);
        }
    }

    public static String logTime(){
        DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        Date date = new Date();
        //System.out.println(dateFormat.format(date));
        return dateFormat.format(date);
    }






}
