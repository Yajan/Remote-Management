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

        Option script = new Option("script",true,"JMX Script");
        script.setRequired(true);
        options.addOption(script);

        Option timer = new Option("t","timer",true,"Start Time in yyyy:MM:dd:hh:mm:ss");
        timer.setRequired(false);
        options.addOption(timer);

        CommandLineParser parser = new DefaultParser();
        HelpFormatter formatter = new HelpFormatter();
        CommandLine cmd;

        try{
            cmd = parser.parse(options,args);
        }catch (ParseException e){
            System.out.println(e.getMessage());
            formatter.printHelp("utility-name",options);

            System.exit(1);
            return;
        }


        String filename = cmd.getOptionValue("script");
        String stime = cmd.getOptionValue("timer");
        System.out.println("Execution started");

        System.out.println(filename);
        System.out.println(stime);
        String time = militime(stime);
        System.out.println(time);
        editJMX(filename,time);

    }

    public static String militime(String time) {
        try {
            DateFormat sdf = new SimpleDateFormat("yyyy:MM:dd:hh:mm:ss");
            Date date = sdf.parse(time);

            Calendar now = Calendar.getInstance();
            TimeZone timeZone = now.getTimeZone();
            System.out.println(timeZone.getDisplayName());

            sdf.setTimeZone(timeZone);

            String militime = String.valueOf(date.getTime());
            System.out.println(militime);
            return militime;
        }catch (Exception  exec){
            return String.valueOf(exec);
        }
    }



    public static void editJMX(String xmlfile,String time){
        try {
            File fXmlFile = new File(xmlfile);
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document doc = dBuilder.parse(fXmlFile);

            //optional, but recommended
            //read this - http://stackoverflow.com/questions/13786607/normalization-in-dom-parsing-with-java-how-does-it-work
            doc.getDocumentElement().normalize();

            System.out.println("Root element :" + doc.getDocumentElement().getNodeName());

            NodeList nList = doc.getElementsByTagName("hashTree");

            Node nNode = null;
            NodeList sList = null;
            for (int temp = 0; temp < nList.getLength(); temp++) {
                nNode = nList.item(temp);
                System.out.println("Sub root Element :" + nNode.getNodeName());
                sList = doc.getElementsByTagName("ThreadGroup");
                break;
            }

            for (int tem = 0; tem < sList.getLength(); tem++) {

                if (nNode.getNodeType() == Node.ELEMENT_NODE) {
                    Node sNode = sList.item(tem);

                    Element eElement = (Element) sNode;
                    System.out.println("Node Element :" + nNode.getNodeName());
                    //System.out.println(eElement.getTagName());

                    // System.out.println("Value : " + eElement.getChildNodes());

                    System.out.println("Bool Value : " + eElement.getElementsByTagName("longProp").item(0).getTextContent());
                    Node timer = eElement.getElementsByTagName("longProp").item(0);
                    timer.setTextContent(time);
                    System.out.println("Bool Value : " + eElement.getElementsByTagName("longProp").item(0).getTextContent());
                    // write the content into xml file
                    TransformerFactory transformerFactory = TransformerFactory.newInstance();
                    Transformer transformer = transformerFactory.newTransformer();
                    DOMSource source = new DOMSource(doc);
                    StreamResult result = new StreamResult(new File(xmlfile));
                    transformer.transform(source, result);

                    System.out.println("Done");
                    break;
                }
            }
        } catch (Exception exec) {
            System.out.println(exec);
        }
    }



}
