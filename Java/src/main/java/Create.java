import java.io.File;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Attr;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

public class Create {

    public static final String xmlFilePath = "HTTPRequest.jmx";

    public static void createJMX(String url){
        String iteration = "10";
        String concurrency = "10";
        String rampup = "1";
        createJMX(url,concurrency,iteration,rampup);
    }

    public static void createJMX(String url,String concurrency, String iteration,String rampup) {

        try {
            String starttime = "1";
            String endtime = "1";


            DocumentBuilderFactory documentFactory = DocumentBuilderFactory.newInstance();

            DocumentBuilder documentBuilder = documentFactory.newDocumentBuilder();

            Document document = documentBuilder.newDocument();

            // root element
            Element root = document.createElement("jmeterTestPlan");
            document.appendChild(root);

            //set an attributed to root element

            Attr jmeter = document.createAttribute("jmeter");
            jmeter.setValue("3.3 r1808647");
            root.setAttributeNode(jmeter);

            Attr properties = document.createAttribute("properties");
            properties.setValue("3.2");
            root.setAttributeNode(properties);

            Attr version = document.createAttribute("version");
            version.setValue("1.2");
            root.setAttributeNode(version);

            // Hash Tree
            Element hashTree = document.createElement("hashTree");
            root.appendChild(hashTree);

                // Test Plan
                Element testplan = document.createElement("TestPlan");
                hashTree.appendChild(testplan);

                Attr enable = document.createAttribute("enabled");
                enable.setValue("true");
                testplan.setAttributeNode(enable);

                Attr guiclass = document.createAttribute("guiclass");
                guiclass.setValue("TestPlanGui");
                testplan.setAttributeNode(guiclass);

                Attr testclass = document.createAttribute("testclass");
                testclass.setValue("TestPlan");
                testplan.setAttributeNode(testclass);

                Attr testname = document.createAttribute("testname");
                testname.setValue("Test Plan");
                testplan.setAttributeNode(testname);


                    // StripProp element
                    Element stringProp = document.createElement("stringProp");
                    testplan.appendChild(stringProp);

                    Attr name = document.createAttribute("name");
                    name.setValue("TestPlan.comments");
                    stringProp.setAttributeNode(name);


                    // boolProp element
                    Element boolProp = document.createElement("boolProp");
                    boolProp.appendChild(document.createTextNode("false"));
                    testplan.appendChild(boolProp);

                    Attr boolname = document.createAttribute("name");
                    boolname.setValue("TestPlan.functional_mode");
                    boolProp.setAttributeNode(boolname);

                    // boolProp element
                    Element boolProp1 = document.createElement("boolProp");
                    boolProp1.appendChild(document.createTextNode("false"));
                    testplan.appendChild(boolProp1);

                    Attr boolname1 = document.createAttribute("name");
                    boolname1.setValue("TestPlan.serialize_threadgroups");
                    boolProp1.setAttributeNode(boolname1);

                    Element elementProp = document.createElement("elementProp");
                    testplan.appendChild(elementProp);

                        Attr elementType = document.createAttribute("elementType");
                        elementType.setValue("Arguments");
                        elementProp.setAttributeNode(elementType);

                        Attr enable1 = document.createAttribute("enabled");
                        enable1.setValue("true");
                        elementProp.setAttributeNode(enable1);

                        Attr guiClass1 = document.createAttribute("guiclass");
                        guiClass1.setValue("ArgumentsPanel");
                        elementProp.setAttributeNode(guiClass1);

                        Attr name1 = document.createAttribute("name");
                        name1.setValue("TestPlan.user_defined_variables");
                        elementProp.setAttributeNode(name1);

                        Attr testclass1 = document.createAttribute("testclass");
                        testclass1.setValue("Arguments");
                        elementProp.setAttributeNode(testclass1);

                        Attr testname1 = document.createAttribute("testname");
                        testname1.setValue("User Defined Variables");
                        elementProp.setAttributeNode(testname1);

                        // collection prop element
                        Element collectionProp = document.createElement("collectionProp");
                        elementProp.appendChild(collectionProp);

                            Attr collectionName = document.createAttribute("name");
                            collectionName.setValue("Arguments.arguments");
                            collectionProp.setAttributeNode(collectionName);

                    // StripProp element
                    Element stringProp1 = document.createElement("stringProp");
                    testplan.appendChild(stringProp1);

                    Attr strname = document.createAttribute("name");
                    strname.setValue("TestPlan.user_define_classpath");
                    stringProp1.setAttributeNode(strname);

            Element hashTree1 = document.createElement("hashTree");
            hashTree.appendChild(hashTree1);

                Element ThreadGroup = document.createElement("ThreadGroup");
                hashTree1.appendChild(ThreadGroup);

                Attr enable2 = document.createAttribute("enabled");
                enable2.setValue("true");
                ThreadGroup.setAttributeNode(enable2);

                Attr guiclass2 = document.createAttribute("guiclass");
                guiclass2.setValue("ThreadGroupGui");
                ThreadGroup.setAttributeNode(guiclass2);

                Attr testclass2 = document.createAttribute("testclass");
                testclass2.setValue("ThreadGroup");
                ThreadGroup.setAttributeNode(testclass2);

                Attr testname2 = document.createAttribute("testname");
                testname2.setValue("Thread Group");
                ThreadGroup.setAttributeNode(testname2);


                    Element tStripProp = document.createElement("stringProp");
                    ThreadGroup.appendChild(tStripProp);

                    Attr sName = document.createAttribute("name");
                    sName.setValue("ThreadGroup.on_sample_error");
                    tStripProp.setAttributeNode(sName);

                    tStripProp.appendChild(document.createTextNode("continue"));

                Element tElementProp = document.createElement("elementProp");
                ThreadGroup.appendChild(tElementProp);

                Attr tElementType = document.createAttribute("elementType");
                tElementType.setValue("LoopController");
                tElementProp.setAttributeNode(tElementType);

                Attr tEnable = document.createAttribute("enabled");
                tEnable.setValue("true");
                tElementProp.setAttributeNode(tEnable);

                Attr tGuiClass = document.createAttribute("guiclass");
                tGuiClass.setValue("LoopControlPanel");
                tElementProp.setAttributeNode(tGuiClass);

                Attr tName = document.createAttribute("name");
                tName.setValue("ThreadGroup.main_controller");
                tElementProp.setAttributeNode(tName);

                Attr tTestclass = document.createAttribute("testclass");
                tTestclass.setValue("LoopController");
                tElementProp.setAttributeNode(tTestclass);

                Attr tTestname = document.createAttribute("testname");
                tTestname.setValue("Loop Controller");
                tElementProp.setAttributeNode(tTestname);

                // Bool prop element
                Element tBoolProp = document.createElement("boolProp");
                tElementProp.appendChild(tBoolProp);

                Attr boolPropName = document.createAttribute("name");
                boolPropName.setValue("LoopController.continue_forever");
                tBoolProp.setAttributeNode(boolPropName);

                tBoolProp.appendChild(document.createTextNode("false"));

                // Bool prop element
                Element tStrProp = document.createElement("stringProp");
                tElementProp.appendChild(tStrProp);

                Attr strPropName = document.createAttribute("name");
                strPropName.setValue("LoopController.loops");
                tStrProp.setAttributeNode(strPropName);

                tStrProp.appendChild(document.createTextNode(iteration));


            // Concurrency element
                Element conProp = document.createElement("stringProp");
                ThreadGroup.appendChild(conProp);

                Attr conName = document.createAttribute("name");
                conName.setValue("ThreadGroup.num_threads");
                conProp.setAttributeNode(conName);

                conProp.appendChild(document.createTextNode(concurrency));

                // Ramp up element
                Element rampProp = document.createElement("stringProp");
                ThreadGroup.appendChild(rampProp);

                Attr rampName = document.createAttribute("name");
                rampName.setValue("ThreadGroup.ramp_time");
                rampProp.setAttributeNode(rampName);

                rampProp.appendChild(document.createTextNode(rampup));

                // Start time
                Element startTimeProp = document.createElement("longProp");
                ThreadGroup.appendChild(startTimeProp);

                Attr startName = document.createAttribute("name");
                startName.setValue("ThreadGroup.start_time");
                startTimeProp.setAttributeNode(startName);

                startTimeProp.appendChild(document.createTextNode(starttime));

                // End time
                Element endTimeProp = document.createElement("longProp");
                ThreadGroup.appendChild(endTimeProp);

                Attr endName = document.createAttribute("name");
                endName.setValue("ThreadGroup.end_time");
                endTimeProp.setAttributeNode(endName);

                endTimeProp.appendChild(document.createTextNode(endtime));

                //bool elements

                Element tBoolProp1 = document.createElement("boolProp");
                ThreadGroup.appendChild(tBoolProp);

                Attr boolName = document.createAttribute("name");
                boolName.setValue("ThreadGroup.scheduler");
                tBoolProp1.setAttributeNode(boolName);

                tBoolProp1.appendChild(document.createTextNode("false"));


                //String Prop
                Element tStrProp1 = document.createElement("stringProp");
                ThreadGroup.appendChild(tStrProp1);

                Attr strName = document.createAttribute("name");
                strName.setValue("ThreadGroup.duration");
                tStrProp1.setAttributeNode(strName);

                //String Prop
                Element tStrProp2 = document.createElement("stringProp");
                ThreadGroup.appendChild(tStrProp2);

                Attr strName1 = document.createAttribute("name");
                strName1.setValue("ThreadGroup.delay");
                tStrProp2.setAttributeNode(strName1);

            Element hashTree2 = document.createElement("hashTree")  ;
            hashTree1.appendChild(hashTree2);

                Element httpSampler = document.createElement("HTTPSamplerProxy");
                hashTree2.appendChild(httpSampler);

                Attr hEnable = document.createAttribute("enabled");
                enable2.setValue("true");
                httpSampler.setAttributeNode(hEnable);

                Attr hGuiclass = document.createAttribute("guiclass");
                hGuiclass.setValue("HttpTestSampleGui");
                httpSampler.setAttributeNode(hGuiclass);

                Attr hTestclass = document.createAttribute("testclass");
                hTestclass.setValue("HTTPSamplerProxy");
                httpSampler.setAttributeNode(hTestclass);

                Attr hTestname = document.createAttribute("testname");
                hTestname.setValue("HTTP Request");
                httpSampler.setAttributeNode(hTestname);

                Element hElementProp = document.createElement("elementProp");
                httpSampler.appendChild(hElementProp);

                    Attr hElementType = document.createAttribute("elementType");
                    hElementType.setValue("Arguments");
                    hElementProp.setAttributeNode(hElementType);

                    Attr hEnable1 = document.createAttribute("enabled");
                    hEnable1.setValue("true");
                    hElementProp.setAttributeNode(hEnable1);

                    Attr hGuiClass = document.createAttribute("guiclass");
                    hGuiClass.setValue("HTTPArgumentsPanel");
                    hElementProp.setAttributeNode(hGuiClass);

                    Attr hName = document.createAttribute("name");
                    hName.setValue("HTTPsampler.Arguments");
                    hElementProp.setAttributeNode(hName);

                    Attr hTestclass1 = document.createAttribute("testclass");
                    hTestclass1.setValue("Arguments");
                    hElementProp.setAttributeNode(hTestclass1);

                    Attr hTestname1 = document.createAttribute("testname");
                    hTestname1.setValue("User Defined Variables");
                    hElementProp.setAttributeNode(hTestname1);

                    Element hCollectionProp = document.createElement("collectionProp");
                    hElementProp.appendChild(hCollectionProp);

                    Attr hColnName = document.createAttribute("name");
                    hColnName.setValue("Arguments.arguments");
                    hCollectionProp.setAttributeNode(hColnName);


                    Element strProp = document.createElement("stringProp");
                    httpSampler.appendChild(strProp);

                    Attr StrName = document.createAttribute("name");
                    StrName.setValue("HTTPSampler.domain");
                    strProp.setAttributeNode(StrName);
                    strProp.appendChild(document.createTextNode(url));

                    Element strProp1 = document.createElement("stringProp");
                    httpSampler.appendChild(strProp1);

                    Attr StrName1 = document.createAttribute("name");
                    StrName1.setValue("HTTPSampler.port");
                    strProp1.setAttributeNode(StrName1);
                    strProp1.appendChild(document.createTextNode(" "));


                    //Element 2
                    Element strProp2 = document.createElement("stringProp");
                    httpSampler.appendChild(strProp2);

                    Attr StrName2 = document.createAttribute("name");
                    StrName2.setValue("HTTPSampler.protocol");
                    strProp2.setAttributeNode(StrName2);
                    strProp2.appendChild(document.createTextNode(" "));


                    //Element 3
                    Element strProp3 = document.createElement("stringProp");
                    httpSampler.appendChild(strProp3);

                    Attr StrName3 = document.createAttribute("name");
                    StrName3.setValue("HTTPSampler.contentEncoding");
                    strProp3.setAttributeNode(StrName3);
                    strProp3.appendChild(document.createTextNode(" "));

                    //Element 4
                    Element strProp4 = document.createElement("stringProp");
                    httpSampler.appendChild(strProp4);

                    Attr StrName4 = document.createAttribute("name");
                    StrName4.setValue("HTTPSampler.path");
                    strProp4.setAttributeNode(StrName4);
                    strProp4.appendChild(document.createTextNode(" "));

                    //Element 5
                    Element strProp5 = document.createElement("stringProp");
                    httpSampler.appendChild(strProp5);

                    Attr StrName5 = document.createAttribute("name");
                    StrName5.setValue("HTTPSampler.method");
                    strProp5.setAttributeNode(StrName5);
                    strProp5.appendChild(document.createTextNode("GET"));


                    // Bool Elements

                    Element bool = document.createElement("boolProp");
                    httpSampler.appendChild(bool);

                    Attr bName = document.createAttribute("name");
                    bName.setValue("HTTPSampler.follow_redirects");
                    bool.setAttributeNode(bName);

                    bool.appendChild(document.createTextNode("true"));

                    Element bool1 = document.createElement("boolProp");
                    httpSampler.appendChild(bool1);

                    Attr bName1 = document.createAttribute("name");
                    bName1.setValue("HTTPSampler.auto_redirects");
                    bool1.setAttributeNode(bName1);

                    bool1.appendChild(document.createTextNode("false"));

                    Element bool2= document.createElement("boolProp");
                    httpSampler.appendChild(bool2);

                    Attr bName2 = document.createAttribute("name");
                    bName2.setValue("HTTPSampler.use_keepalive");
                    bool2.setAttributeNode(bName2);

                    bool2.appendChild(document.createTextNode("true"));


                    Element bool3 = document.createElement("boolProp");
                    httpSampler.appendChild(bool3);

                    Attr bName3 = document.createAttribute("name");
                    bName3.setValue("HTTPSampler.DO_MULTIPART_POST");
                    bool3.setAttributeNode(bName3);

                    bool3.appendChild(document.createTextNode("false"));

            Element eHashtree = document.createElement("hashTree");
            hashTree2.appendChild(eHashtree);

            Element workBench = document.createElement("WorkBench")   ;
            hashTree.appendChild(workBench);

            Attr wEnable = document.createAttribute("enabled");
            wEnable.setValue("true");
            workBench.setAttributeNode(wEnable);

            Attr wGuiClass = document.createAttribute("guiclass");
            wGuiClass.setValue("WorkBenchGui");
            workBench.setAttributeNode(wGuiClass);

            Attr wTestClass = document.createAttribute("testclass");
            wTestClass.setValue("WorkBench");
            workBench.setAttributeNode(wTestClass);

            Attr wTestname = document.createAttribute("testname");
            wTestname.setValue("WorkBench");
            workBench.setAttributeNode(wTestname);

                Element wBool = document.createElement("boolProp");
                workBench.appendChild(wBool);

                Attr wBoolName = document.createAttribute("name");
                wBoolName.setValue("WorkBench.save");
                wBool.setAttributeNode(wBoolName);

                wBool.appendChild(document.createTextNode("true"));

            Element endHashtree = document.createElement("hashTree");
            root.appendChild(endHashtree);




            // create the xml file
            //transform the DOM Object to an XML File
            TransformerFactory transformerFactory = TransformerFactory.newInstance();
            Transformer transformer = transformerFactory.newTransformer();
            DOMSource domSource = new DOMSource(document);
            StreamResult streamResult = new StreamResult(new File(xmlFilePath));

            // If you use
            // StreamResult result = new StreamResult(System.out);
            // the output will be pushed to the standard output ...
            // You can use that for debugging
            transformer.setOutputProperty(OutputKeys.INDENT,"yes");
            transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "2");
            transformer.transform(domSource, streamResult);

            System.out.println("Done creating JMX File");

        } catch (ParserConfigurationException pce) {
            pce.printStackTrace();
        } catch (TransformerException tfe) {
            tfe.printStackTrace();
        }
    }
}