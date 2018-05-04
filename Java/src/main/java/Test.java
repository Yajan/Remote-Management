import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import java.io.File;

public class Test {

    public static void main(String argv[]) {
        try {
            File XmlFile = new File("C:\\Users\\Yajana\\JavaProjects\\IntellJ\\perftool\\src\\main\\resources\\Staff.xml");
            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            DocumentBuilder db = dbf.newDocumentBuilder();
            Document doc = db.parse(XmlFile);
            doc.getDocumentElement().normalize();
            System.out.println("Root element " + doc.getDocumentElement().getNodeName());

            NodeList nodeList=doc.getElementsByTagName("*");
            for (int i=0; i<nodeList.getLength(); i++)
            {
                // Get element
                Element element = (Element)nodeList.item(i);
                System.out.println(element.getNodeName());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

