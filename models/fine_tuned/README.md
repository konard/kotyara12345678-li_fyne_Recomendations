---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:112213
- loss:MultipleNegativesRankingLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: "create react app not creating src folder\n\nHi I am facing problem\
    \ when create-react-app which is not showing src folder unable to start npm start\
    \ \r\n\r\n**Windows PowerShell\r\nCopyright (C) Microsoft Corporation. All rights\
    \ reserved.\r\n\r\nInstall the latest PowerShell for new features and improvements!\
    \ https://aka.ms/PSWindows\r\n\r\nPS F:\\React Js\\REACT-SPRINGBOOT-CRUD> npx\
    \ create-react-app my-app\r\n\r\nCreating a new React app in F:\\React Js\\REACT-SPRINGBOOT-CRUD\\\
    my-app.\r\n\r\nInstalling packages. This might take a couple of minutes.\r\nInstalling\
    \ react, react-dom, and react-scripts with cra-template...\r\n\r\n\r\nadded 1379\
    \ packages in 6m**\r\n\r\n\r\nNot going forward after above"
  sentences:
  - "Hi I am facing problem when create-react-app which is not showing src folder\
    \ unable to start npm start \r\n\r\n**Windows PowerShell\r\nCopyright (C) Microsoft\
    \ Corporation. All rights reserved.\r\n\r\nInstall the latest PowerShell for new\
    \ features and improvements! https://aka.ms/PSWindows\r\n\r\nPS F:\\React Js\\\
    REACT-SPRINGBOOT-CRUD> npx create-react-app my-app\r\n\r\nCreating a new React\
    \ app in F:\\React Js\\REACT-SPRINGBOOT-CRUD\\my-app.\r\n\r\nInstalling packages.\
    \ This might take a couple of minutes.\r\nInstalling react, react-dom, and react-scripts\
    \ with cra-template...\r\n\r\n\r\nadded 1379 packages in 6m**\r\n\r\n\r\nNot going\
    \ forward after above"
  - 'Version: 1.3.7

    CUPS.org User: martin.pitt.canonical


    From http://bugs.debian.org/379014:


    "According to cupsd.conf(5), the HostNameLookups option takes

    Yes or No as values; these should be On or Off (using Yes or

    No results in an "unknown value" error in /var/log/cups/error.log"'
  - 0.9.3版本生成的二维码在华为手机上打开 有小方格   有一格一格的小方格  导致识别不了， 0.9.2无问题  使用代码如此`<QRCode value={qrcode}
    size={155} />`
- source_sentence: "create-react-app does not clean up directory after failed install\
    \ on Windows\n\nWhen the CLI fails to create a new application, it should cleanup\
    \ and delete the directory it had created.\r\n\r\nPlease help us fix this bug\
    \ or resolve the test case!\r\n\r\nhttps://github.com/facebookincubator/create-react-app/blob/master/tasks/e2e-installs.sh#L126-L130"
  sentences:
  - "When the CLI fails to create a new application, it should cleanup and delete\
    \ the directory it had created.\r\n\r\nPlease help us fix this bug or resolve\
    \ the test case!\r\n\r\nhttps://github.com/facebookincubator/create-react-app/blob/master/tasks/e2e-installs.sh#L126-L130"
  - 'In order to ship #111, we want to call the API when a version is selected in
    the `VersionChooser` component. This action will also update the URL.'
  - "Please add Handled with var in Publisher OnGetValuationDateOnBeforeFindOldValueEntry(OldValueEntry,\
    \ **var Handled**);\r\n\r\n//OnGetValuationDateOnBeforeFindOldValueEntry(OldValueEntry);\r\
    \nHandled := FALSE;\r\nOnGetValuationDateOnBeforeFindOldValueEntry(OldValueEntry,Handled);\r\
    \nIF Handled THEN   \r\n  EXIT; \r\n\r\n\r\nPlease add OnBeforeInitValueEntry\
    \ publisher in function InitValueEntry in cu22\r\nOnBeforeInitValueEntry(ValueEntry,ItemJnlLine,ValueEntryNo);\r\
    \nValueEntryNo is the global variable with var"
- source_sentence: "\"Unused pure expression or super\"\n\nThe following code is generating\
    \ this warning. The only work-around that I could come up with is to use a function\
    \ to initialize the affected const expression.\r\n\r\n```\r\nLeft operand of &&\
    \ operator is always falsy.\r\nconst DOTTED_LINE = (/* unused pure expression\
    \ or super */ null && ([2, 2]));\r\n```\r\n\r\nThe code: \r\n```\r\nexport const\
    \ DASHED_LINE = [7, 3];\r\nexport const DOT_DASH_LINE = [7, 2, 2, 2];\r\nexport\
    \ const DOTTED_LINE = [2, 2];\r\n```\r\n\r\nI'm using these flags:\r\n\r\n```\r\
    \ncompilation_level: 'ADVANCED'\r\nuse_types_for_optimization: true\r\n```"
  sentences:
  - "Hi dev team, please add in Codeunit 12179,  the ClientFileName variable to the\
    \ exposed event OnAfterCreateBlobXML, contained in the procedure GenerateXMLFile.\r\
    \n\r\n \r\n    procedure GenerateXMLFile(var TempBlob: Codeunit \"Temp Blob\"\
    ; var TempFatturaLine: Record \"Fattura Line\" temporary; TempFatturaHeader: Record\
    \ \"Fattura Header\" temporary; ClientFileName: Text[250])\r\n    var\r\n    \
    \    ExportFatturaPADocument: Codeunit \"Export FatturaPA Document\";\r\n    begin\r\
    \n            ........\r\n            ........\r\n            ........\r\n   \
    \         \r\n                    // update Buffer\r\n                    TempXMLBuffer.FindFirst();\r\
    \n                    TempXMLBuffer.Save(TempBlob);\r\n\r\n                  \
    \  OnAfterCreateBlobXML(TempXMLBuffer, TempBlob);                       //AS IS\r\
    \n                    \r\n              *********************************REQUEST\
    \  TO BE     *************************\r\n                   OnAfterCreateBlobXML(TempXMLBuffer,\
    \ TempBlob, ClientFileName);  \r\n\r\n            ******************************************************************************\r\
    \n\r\n           ........\r\n    end;\r\n\r\n\r\nin the previous version of the\
    \ procedure, the exposed event had the filename.\r\nyou probably chose not to\
    \ display it, but it is very useful.\r\nThank you"
  - "The following code is generating this warning. The only work-around that I could\
    \ come up with is to use a function to initialize the affected const expression.\r\
    \n\r\n```\r\nLeft operand of && operator is always falsy.\r\nconst DOTTED_LINE\
    \ = (/* unused pure expression or super */ null && ([2, 2]));\r\n```\r\n\r\nThe\
    \ code: \r\n```\r\nexport const DASHED_LINE = [7, 3];\r\nexport const DOT_DASH_LINE\
    \ = [7, 2, 2, 2];\r\nexport const DOTTED_LINE = [2, 2];\r\n```\r\n\r\nI'm using\
    \ these flags:\r\n\r\n```\r\ncompilation_level: 'ADVANCED'\r\nuse_types_for_optimization:\
    \ true\r\n```"
  - "Hello,\r\n\r\n## Problem\r\n\r\nThis issue is related to #1022, #102 and probably\
    \ some others.\r\nI believe that many people would like to have an option to use\
    \ any variables they want, not just prefixed with `REACT_APP_`. This is especially\
    \ important for building applications on external systems, where they dictate\
    \ you the variables.\r\n\r\n## Possible solutions\r\n\r\nI believe, there are\
    \ more ways to solve the issue. There are few of them.\r\n\r\n### Use additional\
    \ environment variable to remove REACT_APP_ prefix filter.\r\nUse `process.env.ALLOW_CUSTOM_ENV_VARS=true`\
    \ to change/remove the filtering condition in [env.js](https://github.com/facebook/create-react-app/blob/v2.1.1/packages/react-scripts/config/env.js#L73)\r\
    \n\r\n### Allow using the result of dotenv.load() in source code\r\n`dotenv.load()`\
    \ results in an object with either `parsed` or `error` key. `parsed` object holds\
    \ all variables that were loaded from the current dotenv file. Allow them to be\
    \ used in application regardless of prefix, while already existing env vars will\
    \ only be included if they have `REACT_APP_` prefix.\r\n\r\n### Simple. Easy.\r\
    \nJust remove `.filter(key => REACT_APP.test(key))` code. I doubt it'll slow down\
    \ compilation speed dramatically. This is my favorite.\r\n\r\n/cc @Timer @gaearon\
    \ @iansu"
- source_sentence: "Parsing shared library name fails on MacOS\n\nSince https://github.com/tensorflow/tensorflow/commit/7efc61175c540a56b03e829ec917ce9efc1f06f9\
    \ custom-op's configure script will no longer properly parse the shared library\
    \ name for macos TensorFlow:\r\nhttps://github.com/tensorflow/custom-op/blob/master/configure.sh#L94\r\
    \n\r\nAs a quick fix in Addons we just [altered the string parsing to be OS dependent](https://github.com/tensorflow/addons/pull/357/files),\
    \ but a more elegant solution is probably possible. I tried passing the linkflag\
    \ to copts but ran into issues without copying the library to the bazel build\
    \ dir as a GENRULE. \r\n\r\nHappy to submit a string parsing PR to fix to this\
    \ repo; or modify the Addons script to match a better solution that comes from\
    \ this."
  sentences:
  - "<!--\r\nPlease add the affected binary name in the title unless multiple binaries\
    \ are affected, e.g.\r\n[cinder-csi-plugin] Cannot delete PV\r\nFor openstack-cloud-controller-manager,\
    \ you can use [occm] for short.\r\n\r\nAll the currently maintained binaries are:\r\
    \n* openstack-cloud-controller-manager (occm)\r\n* cinder-csi-plugin\r\n* manila-csi-plugin\r\
    \n* k8s-keystone-auth\r\n* client-keystone-auth\r\n* octavia-ingress-controller\r\
    \n* magnum-auto-healer\r\n* barbican-kms-plugin\r\n-->\r\n\r\n**Is this a BUG\
    \ REPORT or FEATURE REQUEST?**:\r\n\r\n> Uncomment only one, leave it on its own\
    \ line: \r\n>\r\n> /kind bug\r\n> /kind feature\r\n\r\n**What happened**:\r\n\r\
    \nI cann't build image from makefile, someone can help me to write down here some\
    \ commands to build this images \r\n\r\n\r\n**What you expected to happen**:\r\
    \n\r\n\r\n**How to reproduce it**:\r\n\r\n\r\n**Anything else we need to know?**:\r\
    \n\r\n\r\n**Environment**:\r\n- openstack-cloud-controller-manager(or other related\
    \ binary) version:\r\n- OpenStack version:\r\n- Others:"
  - "Hey folks, :wave:\r\n\r\n### Describe the problem and steps to reproduce it:\r\
    \n\r\nWe ran into an issue with uploading and signing our unlisted, self-deployed\
    \ extension:\r\n\r\n> web-ext sign --source-dir build --channel \"unlisted\" --artifacts-dir\
    \ dist/firefox --id \"firefox@heylogin.com\"\r\n\r\n### What happened?\r\n\r\n\
    The command uploads the extension, and receives a validation report, but then\
    \ times out. On AMO the version is listed as \"Awaiting Review\", which hasn't\
    \ changed in several days now. This happened consistently in a couple of attempts,\
    \ including one with the exact same code submitted that was auto-approved before.\r\
    \n\r\n### What did you expect to happen?\r\n\r\nThis command produced a signed\
    \ xpi within ~5 minutes from an automatic validation. This worked well for several\
    \ months.\r\n\r\n### Anything else we should know?\r\n\r\nThis command was being\
    \ called as part of our CI pipeline, sometimes up to a couple of times per day.\
    \ The `web-ext sign` documentation included no specifics about whether that's\
    \ a legitimate use, using it in this way worked for several months without issues\
    \ for us.\r\n\r\nI don't know if this is a rate limiting issue or not, but it\
    \ would be good to include a paragraph about the expected use of the API so developers\
    \ can use it with confidence that they are not overstepping some unknown boundaries."
  - "Since https://github.com/tensorflow/tensorflow/commit/7efc61175c540a56b03e829ec917ce9efc1f06f9\
    \ custom-op's configure script will no longer properly parse the shared library\
    \ name for macos TensorFlow:\r\nhttps://github.com/tensorflow/custom-op/blob/master/configure.sh#L94\r\
    \n\r\nAs a quick fix in Addons we just [altered the string parsing to be OS dependent](https://github.com/tensorflow/addons/pull/357/files),\
    \ but a more elegant solution is probably possible. I tried passing the linkflag\
    \ to copts but ran into issues without copying the library to the bazel build\
    \ dir as a GENRULE. \r\n\r\nHappy to submit a string parsing PR to fix to this\
    \ repo; or modify the Addons script to match a better solution that comes from\
    \ this."
- source_sentence: "[Event Request] Codeunit 370 \"Bank Acc. Reconciliation Post\"\
    \  ApplyCustLedgEntry, ApplyVendLedgEntry and ApplyEmployeeLedgEntry\n\nPlease\
    \ add an event with a handled pattern in procedures ApplyCustLedgEntry, ApplyVendLedgEntry\
    \ and ApplyEmployeeLedgEntry before applying the ledger entry:\r\n```\r\n    [IntegrationEvent(false,\
    \ false)]\r\n    local procedure OnBeforeApplyCustLedgEntry(var CustLedgerEntry:\
    \ Record \"Cust. Ledger Entry\"; AppliedPmtEntry: Record \"Applied Payment Entry\"\
    ; var BankAcc: Record \"Bank Account\"; AppliesToID: Code[50]; PostingDate: Date;\
    \ PmtDiscDueDate: Date; PmtDiscToleranceDate: Date; RemPmtDiscPossible: Decimal;\
    \ var Handled: Boolean);\r\n    begin\r\n    end;\r\n```\r\n\r\nAnd raise the\
    \ event in the procedures ApplyCustLedgEntry, ApplyVendLedgEntry and ApplyEmployeeLedgEntry.\
    \ See example below:\r\n\r\n```\r\n    procedure ApplyCustLedgEntry(AppliedPmtEntry:\
    \ Record \"Applied Payment Entry\"; AppliesToID: Code[50]; PostingDate: Date;\
    \ PmtDiscDueDate: Date; PmtDiscToleranceDate: Date; RemPmtDiscPossible: Decimal)\r\
    \n    var\r\n        CustLedgEntry: Record \"Cust. Ledger Entry\";\r\n       \
    \ CurrExchRate: Record \"Currency Exchange Rate\";\r\n        IsHandled: Boolean;\r\
    \n    begin\r\n        with CustLedgEntry do begin\r\n            Get(AppliedPmtEntry.\"\
    Applies-to Entry No.\");\r\n            TestField(Open);\r\n            BankAcc.Get(AppliedPmtEntry.\"\
    Bank Account No.\");\r\n            OnBeforeApplyCustLedgEntry(CustLedgEntry,\
    \ AppliedPmtEntry, BankAcc, AppliesToID, PostingDate, PmtDiscDueDate, PmtDiscToleranceDate,\
    \ RemPmtDiscPossible, IsHandled);\r\n            if IsHandled then\r\n       \
    \         exit;\r\n\r\n            if AppliesToID = '' then begin\r\n        \
    \        \"Pmt. Discount Date\" := PmtDiscDueDate;\r\n                \"Pmt. Disc.\
    \ Tolerance Date\" := PmtDiscToleranceDate;\r\n\r\n                \"Remaining\
    \ Pmt. Disc. Possible\" := RemPmtDiscPossible;\r\n                if BankAcc.IsInLocalCurrency()\
    \ then\r\n                    \"Remaining Pmt. Disc. Possible\" :=\r\n       \
    \               CurrExchRate.ExchangeAmount(\"Remaining Pmt. Disc. Possible\"\
    , '', \"Currency Code\", PostingDate);\r\n            end else begin\r\n     \
    \           \"Applies-to ID\" := AppliesToID;\r\n                \"Amount to Apply\"\
    \ := AppliedPmtEntry.CalcAmountToApply(PostingDate);\r\n            end;\r\n\r\
    \n            if PreviewMode then\r\n                CustEntryEditNoCommit(CustLedgEntry)\r\
    \n            else\r\n                CODEUNIT.Run(CODEUNIT::\"Cust. Entry-Edit\"\
    , CustLedgEntry);\r\n        end;\r\n    end;\r\n```\r\n\r\nThank you in advance."
  sentences:
  - "Please add an event with a handled pattern in procedures ApplyCustLedgEntry,\
    \ ApplyVendLedgEntry and ApplyEmployeeLedgEntry before applying the ledger entry:\r\
    \n```\r\n    [IntegrationEvent(false, false)]\r\n    local procedure OnBeforeApplyCustLedgEntry(var\
    \ CustLedgerEntry: Record \"Cust. Ledger Entry\"; AppliedPmtEntry: Record \"Applied\
    \ Payment Entry\"; var BankAcc: Record \"Bank Account\"; AppliesToID: Code[50];\
    \ PostingDate: Date; PmtDiscDueDate: Date; PmtDiscToleranceDate: Date; RemPmtDiscPossible:\
    \ Decimal; var Handled: Boolean);\r\n    begin\r\n    end;\r\n```\r\n\r\nAnd raise\
    \ the event in the procedures ApplyCustLedgEntry, ApplyVendLedgEntry and ApplyEmployeeLedgEntry.\
    \ See example below:\r\n\r\n```\r\n    procedure ApplyCustLedgEntry(AppliedPmtEntry:\
    \ Record \"Applied Payment Entry\"; AppliesToID: Code[50]; PostingDate: Date;\
    \ PmtDiscDueDate: Date; PmtDiscToleranceDate: Date; RemPmtDiscPossible: Decimal)\r\
    \n    var\r\n        CustLedgEntry: Record \"Cust. Ledger Entry\";\r\n       \
    \ CurrExchRate: Record \"Currency Exchange Rate\";\r\n        IsHandled: Boolean;\r\
    \n    begin\r\n        with CustLedgEntry do begin\r\n            Get(AppliedPmtEntry.\"\
    Applies-to Entry No.\");\r\n            TestField(Open);\r\n            BankAcc.Get(AppliedPmtEntry.\"\
    Bank Account No.\");\r\n            OnBeforeApplyCustLedgEntry(CustLedgEntry,\
    \ AppliedPmtEntry, BankAcc, AppliesToID, PostingDate, PmtDiscDueDate, PmtDiscToleranceDate,\
    \ RemPmtDiscPossible, IsHandled);\r\n            if IsHandled then\r\n       \
    \         exit;\r\n\r\n            if AppliesToID = '' then begin\r\n        \
    \        \"Pmt. Discount Date\" := PmtDiscDueDate;\r\n                \"Pmt. Disc.\
    \ Tolerance Date\" := PmtDiscToleranceDate;\r\n\r\n                \"Remaining\
    \ Pmt. Disc. Possible\" := RemPmtDiscPossible;\r\n                if BankAcc.IsInLocalCurrency()\
    \ then\r\n                    \"Remaining Pmt. Disc. Possible\" :=\r\n       \
    \               CurrExchRate.ExchangeAmount(\"Remaining Pmt. Disc. Possible\"\
    , '', \"Currency Code\", PostingDate);\r\n            end else begin\r\n     \
    \           \"Applies-to ID\" := AppliesToID;\r\n                \"Amount to Apply\"\
    \ := AppliedPmtEntry.CalcAmountToApply(PostingDate);\r\n            end;\r\n\r\
    \n            if PreviewMode then\r\n                CustEntryEditNoCommit(CustLedgEntry)\r\
    \n            else\r\n                CODEUNIT.Run(CODEUNIT::\"Cust. Entry-Edit\"\
    , CustLedgEntry);\r\n        end;\r\n    end;\r\n```\r\n\r\nThank you in advance."
  - "<!--\nRead the contributing https://github.com/microsoft/AL/blob/master/CONTRIBUTING.md\
    \ guide before proceeding\n\nPlease follow this template in order for our developers\
    \ to investigate your issue efficiently.\n\nDo not edit or remove the titles;\
    \ e.g. \"Describe the bug\".\n\nUse the latest version of the AL language extension\
    \ from the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-dynamics-smb.al)\
    \ or shipped as part of the [AL Developer Preview builds](README.md#al-developer-preview-builds)\
    \ for Dynamics 365 Business Central.\n\nDisable all extensions except the AL Language\
    \ extension.\n\n-->\n\nPlease include the following with each issue:\n\n**1. Describe\
    \ the bug**\nI created a multi app workspace and utilised the new directory.apps.props.json\
    \ file to set various properties in my apps.  One property in particular is not\
    \ flowing through to the compiled app file.  The property in question is runtime\
    \ property.\n\nI set runtime to 15.2 in the directory.apps.props.json file and\
    \ removed it from App.json in App1 but left it there in App2 and App3 app.json\
    \ files.  \n\nMy expectation is that app1 compile artifact (*.app) will be compiled\
    \ to the value set by directory.apps.props.json (since it's own app.json does\
    \ not specify the runtime property.  App2 and App3 compiled app files will contain\
    \ the runtime value from their respective app.json files since the runtime property\
    \ is present there.\n\nHowever, when I build App1 (expecting runtime 15.2 as defined\
    \ in directory.apps.props.json) it actually gets a runtime of 17.\n\n**2. To Reproduce**\n\
    1. Create a multi project workspace with 3 app folders.\n2. Create a directory.app.props.json\
    \ \n```\n{\n    \"variables\": {\n        \"major\": \"25\",\n        \"minor\"\
    : \"1\",\n        \"build\": \"1\",\n        \"revision\": \"2\",\n        \"\
    version\": \"$(major).$(minor).$(build).$(revision)\"\n    },\n    \"properties\"\
    : {\n        \"publisher\": \"Fabrikam\",\n        \"runtime\": \"15.2\",\n  \
    \      \"application\": \"25.0.0.0\",\n        \"platform\": \"25.0.0.0\"\n  \
    \  }\n}\n```\n3. edit App1's app.json to remove publisher, runtime, application\
    \ and platform properties.\n4. compile App1\n5. open compiled app in 7zip\n6.\
    \ open NavxManifest.xml and check the values and see that all are set based off\
    \ properties in  directory.app.props.json EXCEPT runtime, which should be 15.2\
    \ but is actually 17.0\n```\n<Package xmlns=\"http://schemas.microsoft.com/navx/2015/manifest\"\
    >\n<App Id=\"c9f93b54-869f-4b75-8242-0d8236b21ec1\" Name=\"App1\" Publisher=\"\
    Fabrikam\" Brief=\"\" Description=\"\" Version=\"25.1.1.2\" CompatibilityId=\"\
    0.0.0.0\" PrivacyStatement=\"\" EULA=\"\" Help=\"\" HelpBaseUrl=\"\" Url=\"\"\
    \ Logo=\"\" Platform=\"25.0.0.0\" Application=\"25.0.0.0\" Runtime=\"17.0\" Target=\"\
    Cloud\" ShowMyCode=\"False\"/>\n<IdRanges>\n<IdRange MinObjectId=\"50100\" MaxObjectId=\"\
    50149\"/>\n</IdRanges>\n<Dependencies/>\n<InternalsVisibleTo/>\n<ScreenShots/>\n\
    <SupportedLocales/>\n<Features>\n<Feature>NOIMPLICITWITH</Feature>\n</Features>\n\
    <PreprocessorSymbols/>\n<SuppressWarnings/>\n<ResourceExposurePolicy AllowDebugging=\"\
    true\" AllowDownloadingSource=\"true\" IncludeSourceInSymbolFile=\"true\" ApplyToDevExtension=\"\
    false\"/>\n<KeyVaultUrls/>\n<Source/>\n<Build By=\"AL Language Extension,17.0.1860968\"\
    \ Timestamp=\"2025-10-20T05:50:16.6536797Z\" CompilerVersion=\"17.0.28.26016\"\
    />\n<AlternateIds/>\n</Package>\n```\n\n\n\nRepo containing my sample that demonstrates\
    \ the issue\nhttps://github.com/Professional-Advantage-SDG/Props-Json-Spike\n\n\
    [directory.app.props.json](https://github.com/user-attachments/files/22996209/directory.app.props.json)\n\
    \n**Note:** Because the developers need to copy and paste the code snippet, including\
    \ a code snippet as a media file (i.e. .gif) is not sufficient.\n\n**3. Expected\
    \ behavior**\nExpecting compiled app to contain the runtime value set in the directory.app.props.json\
    \ file\n\n**4. Actual behavior**\nmanifest contains runtime 17.0 and attempting\
    \ to install the app into a BC version 26 environment results in an error regarding\
    \ runtime and version 17,\n\n**5. Versions:**\n\n- AL Language: 17.0.1860968\n\
    - Visual Studio Code: 1.105.1\n- Business Central: v26.5\n- List of Visual Studio\
    \ Code extensions that you have installed: AL\n- Operating System:\n  * [X] Windows\n\
    \  * [ ] Linux\n  * [ ] MacOS\n\n### Final Checklist\n\nPlease remember to do\
    \ the following:\n\n* [X] Search the issue repository to ensure you are reporting\
    \ a new issue\n\n* [X] Reproduce the issue after disabling all extensions except\
    \ the AL Language extension\n\n* [X] Simplify your code around the issue to better\
    \ isolate the problem\n\nInternal work item: [AB#611205](https://dynamicssmb2.visualstudio.com/1fcb79e7-ab07-432a-a3c6-6cf5a88ba4a5/_workitems/edit/611205)"
  - "## Environment\r\n\r\nDescribe your dev environment here, giving as many details\
    \ as possible. If you have them, make sure to include:\r\n\r\n- Unity Editor Version:\
    \ `2023.2.16f1`\r\n- Unity SDK Version: `16.0.2`\r\n\r\n## The SDK DLLs are not\
    \ compatible with 2023.2.16f1\r\n\r\nAssembly 'Assets/FacebookSDK/Plugins/Windows/Facebook.Unity.Windows.dll'\
    \ will not be loaded due to errors:\r\nReference has errors 'Facebook.Unity'.\r\
    \n\r\nAssembly 'Assets/FacebookSDK/Plugins/Editor/Facebook.Unity.Editor.dll' will\
    \ not be loaded due to errors:\r\nReference has errors 'Facebook.Unity'.\r\n\r\
    \nAssembly 'Assets/FacebookSDK/Plugins/Canvas/Facebook.Unity.Canvas.dll' will\
    \ not be loaded due to errors:\r\nReference has errors 'Facebook.Unity'.\r\n\r\
    \nAssembly 'Assets/FacebookSDK/Plugins/Facebook.Unity.dll' will not be loaded\
    \ due to errors:\r\nUnable to resolve reference 'UnityEngine.UI'. Is the assembly\
    \ missing or incompatible with the current platform?\r\n\r\nScreenshot of errors\
    \ in Unity Console.\r\n![image](https://github.com/facebook/facebook-sdk-for-unity/assets/10584204/94e6c32b-1f6c-42dc-87b6-aedf829f3d69)"
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision c9745ed1d9f207416be6d2e6f8de32d1f16199bf -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    '[Event Request] Codeunit 370 "Bank Acc. Reconciliation Post"  ApplyCustLedgEntry, ApplyVendLedgEntry and ApplyEmployeeLedgEntry\n\nPlease add an event with a handled pattern in procedures ApplyCustLedgEntry, ApplyVendLedgEntry and ApplyEmployeeLedgEntry before applying the ledger entry:\r\n```\r\n    [IntegrationEvent(false, false)]\r\n    local procedure OnBeforeApplyCustLedgEntry(var CustLedgerEntry: Record "Cust. Ledger Entry"; AppliedPmtEntry: Record "Applied Payment Entry"; var BankAcc: Record "Bank Account"; AppliesToID: Code[50]; PostingDate: Date; PmtDiscDueDate: Date; PmtDiscToleranceDate: Date; RemPmtDiscPossible: Decimal; var Handled: Boolean);\r\n    begin\r\n    end;\r\n```\r\n\r\nAnd raise the event in the procedures ApplyCustLedgEntry, ApplyVendLedgEntry and ApplyEmployeeLedgEntry. See example below:\r\n\r\n```\r\n    procedure ApplyCustLedgEntry(AppliedPmtEntry: Record "Applied Payment Entry"; AppliesToID: Code[50]; PostingDate: Date; PmtDiscDueDate: Date; PmtDiscToleranceDate: Date; RemPmtDiscPossible: Decimal)\r\n    var\r\n        CustLedgEntry: Record "Cust. Ledger Entry";\r\n        CurrExchRate: Record "Currency Exchange Rate";\r\n        IsHandled: Boolean;\r\n    begin\r\n        with CustLedgEntry do begin\r\n            Get(AppliedPmtEntry."Applies-to Entry No.");\r\n            TestField(Open);\r\n            BankAcc.Get(AppliedPmtEntry."Bank Account No.");\r\n            OnBeforeApplyCustLedgEntry(CustLedgEntry, AppliedPmtEntry, BankAcc, AppliesToID, PostingDate, PmtDiscDueDate, PmtDiscToleranceDate, RemPmtDiscPossible, IsHandled);\r\n            if IsHandled then\r\n                exit;\r\n\r\n            if AppliesToID = \'\' then begin\r\n                "Pmt. Discount Date" := PmtDiscDueDate;\r\n                "Pmt. Disc. Tolerance Date" := PmtDiscToleranceDate;\r\n\r\n                "Remaining Pmt. Disc. Possible" := RemPmtDiscPossible;\r\n                if BankAcc.IsInLocalCurrency() then\r\n                    "Remaining Pmt. Disc. Possible" :=\r\n                      CurrExchRate.ExchangeAmount("Remaining Pmt. Disc. Possible", \'\', "Currency Code", PostingDate);\r\n            end else begin\r\n                "Applies-to ID" := AppliesToID;\r\n                "Amount to Apply" := AppliedPmtEntry.CalcAmountToApply(PostingDate);\r\n            end;\r\n\r\n            if PreviewMode then\r\n                CustEntryEditNoCommit(CustLedgEntry)\r\n            else\r\n                CODEUNIT.Run(CODEUNIT::"Cust. Entry-Edit", CustLedgEntry);\r\n        end;\r\n    end;\r\n```\r\n\r\nThank you in advance.',
    'Please add an event with a handled pattern in procedures ApplyCustLedgEntry, ApplyVendLedgEntry and ApplyEmployeeLedgEntry before applying the ledger entry:\r\n```\r\n    [IntegrationEvent(false, false)]\r\n    local procedure OnBeforeApplyCustLedgEntry(var CustLedgerEntry: Record "Cust. Ledger Entry"; AppliedPmtEntry: Record "Applied Payment Entry"; var BankAcc: Record "Bank Account"; AppliesToID: Code[50]; PostingDate: Date; PmtDiscDueDate: Date; PmtDiscToleranceDate: Date; RemPmtDiscPossible: Decimal; var Handled: Boolean);\r\n    begin\r\n    end;\r\n```\r\n\r\nAnd raise the event in the procedures ApplyCustLedgEntry, ApplyVendLedgEntry and ApplyEmployeeLedgEntry. See example below:\r\n\r\n```\r\n    procedure ApplyCustLedgEntry(AppliedPmtEntry: Record "Applied Payment Entry"; AppliesToID: Code[50]; PostingDate: Date; PmtDiscDueDate: Date; PmtDiscToleranceDate: Date; RemPmtDiscPossible: Decimal)\r\n    var\r\n        CustLedgEntry: Record "Cust. Ledger Entry";\r\n        CurrExchRate: Record "Currency Exchange Rate";\r\n        IsHandled: Boolean;\r\n    begin\r\n        with CustLedgEntry do begin\r\n            Get(AppliedPmtEntry."Applies-to Entry No.");\r\n            TestField(Open);\r\n            BankAcc.Get(AppliedPmtEntry."Bank Account No.");\r\n            OnBeforeApplyCustLedgEntry(CustLedgEntry, AppliedPmtEntry, BankAcc, AppliesToID, PostingDate, PmtDiscDueDate, PmtDiscToleranceDate, RemPmtDiscPossible, IsHandled);\r\n            if IsHandled then\r\n                exit;\r\n\r\n            if AppliesToID = \'\' then begin\r\n                "Pmt. Discount Date" := PmtDiscDueDate;\r\n                "Pmt. Disc. Tolerance Date" := PmtDiscToleranceDate;\r\n\r\n                "Remaining Pmt. Disc. Possible" := RemPmtDiscPossible;\r\n                if BankAcc.IsInLocalCurrency() then\r\n                    "Remaining Pmt. Disc. Possible" :=\r\n                      CurrExchRate.ExchangeAmount("Remaining Pmt. Disc. Possible", \'\', "Currency Code", PostingDate);\r\n            end else begin\r\n                "Applies-to ID" := AppliesToID;\r\n                "Amount to Apply" := AppliedPmtEntry.CalcAmountToApply(PostingDate);\r\n            end;\r\n\r\n            if PreviewMode then\r\n                CustEntryEditNoCommit(CustLedgEntry)\r\n            else\r\n                CODEUNIT.Run(CODEUNIT::"Cust. Entry-Edit", CustLedgEntry);\r\n        end;\r\n    end;\r\n```\r\n\r\nThank you in advance.',
    "## Environment\r\n\r\nDescribe your dev environment here, giving as many details as possible. If you have them, make sure to include:\r\n\r\n- Unity Editor Version: `2023.2.16f1`\r\n- Unity SDK Version: `16.0.2`\r\n\r\n## The SDK DLLs are not compatible with 2023.2.16f1\r\n\r\nAssembly 'Assets/FacebookSDK/Plugins/Windows/Facebook.Unity.Windows.dll' will not be loaded due to errors:\r\nReference has errors 'Facebook.Unity'.\r\n\r\nAssembly 'Assets/FacebookSDK/Plugins/Editor/Facebook.Unity.Editor.dll' will not be loaded due to errors:\r\nReference has errors 'Facebook.Unity'.\r\n\r\nAssembly 'Assets/FacebookSDK/Plugins/Canvas/Facebook.Unity.Canvas.dll' will not be loaded due to errors:\r\nReference has errors 'Facebook.Unity'.\r\n\r\nAssembly 'Assets/FacebookSDK/Plugins/Facebook.Unity.dll' will not be loaded due to errors:\r\nUnable to resolve reference 'UnityEngine.UI'. Is the assembly missing or incompatible with the current platform?\r\n\r\nScreenshot of errors in Unity Console.\r\n![image](https://github.com/facebook/facebook-sdk-for-unity/assets/10584204/94e6c32b-1f6c-42dc-87b6-aedf829f3d69)",
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[ 1.0000,  0.9225, -0.0784],
#         [ 0.9225,  1.0000, -0.1062],
#         [-0.0784, -0.1062,  1.0000]])
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 112,213 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                         | sentence_1                                                                          | label                                                         |
  |:--------|:-----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:--------------------------------------------------------------|
  | type    | string                                                                             | string                                                                              | float                                                         |
  | details | <ul><li>min: 4 tokens</li><li>mean: 177.8 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 2 tokens</li><li>mean: 170.65 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 1.0</li><li>mean: 1.0</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | label            |
  |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
  | <code>User profile notifications are not loading for developer accounts<br><br>### Describe the problem and steps to reproduce it:<br>1. Login on AMO -dev with a developer account<br>1. Go to the Edit profile page<br>1. Check the user Notifications section at the bottom of the page<br><br>### What happened?<br>The notifications section is not loading. The API request to `https://addons-dev.allizom.org/api/v5/accounts/account/<account_id>/notifications/?lang=en-US` returns a 500 error<br>![image](https://user-images.githubusercontent.com/31961530/200338325-a1923946-418a-4e89-9b3e-cf224e99258a.png)<br><br>### What did you expect to happen?<br>User notifications are loading<br><br>### Anything else we should know?<br>When this issue happened in the past, we had to contact someone at basket to investigate. Not sure if the same process applies today.<br>The issue is reproducing only on -dev so far.<br><br><br><br>┆Issue is synchronized with this [Jira Task](https://mozilla-hub.atlassian.net/browse/AMOENG-191)</code> | <code>### Describe the problem and steps to reproduce it:<br>1. Login on AMO -dev with a developer account<br>1. Go to the Edit profile page<br>1. Check the user Notifications section at the bottom of the page<br><br>### What happened?<br>The notifications section is not loading. The API request to `https://addons-dev.allizom.org/api/v5/accounts/account/<account_id>/notifications/?lang=en-US` returns a 500 error<br>![image](https://user-images.githubusercontent.com/31961530/200338325-a1923946-418a-4e89-9b3e-cf224e99258a.png)<br><br>### What did you expect to happen?<br>User notifications are loading<br><br>### Anything else we should know?<br>When this issue happened in the past, we had to contact someone at basket to investigate. Not sure if the same process applies today.<br>The issue is reproducing only on -dev so far.<br><br><br><br>┆Issue is synchronized with this [Jira Task](https://mozilla-hub.atlassian.net/browse/AMOENG-191)</code> | <code>1.0</code> |
  | <code>Can I record call locally in-app? not on server but on the device<br><br>Can I record call locally in-app? not on server but on the device. I mean just record the call even if is just the voice?  <br>Thanks</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <code>Can I record call locally in-app? not on server but on the device. I mean just record the call even if is just the voice?  <br>Thanks</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | <code>1.0</code> |
  | <code>[GENERAL SUPPORT]: Disable logging messages<br><br>### Question<br><br>Hello,<br><br>Is there a simple way to suppress the following logging message without manually adjusting the class?<br><br>https://github.com/facebook/Ax/blob/main/ax/core/experiment.py#L59<br><br>method: attach_trial()<br><br>        logger.info(<br>            "Attached custom parameterizations "<br>            f"{round_floats_for_logging(item=parameterizations)} "<br>            f"as trial {trial.index}."<br>        )<br><br>Such as using verbose_logging=False to suppress the message of a completed trial.<br><br>Thanks in advance!<br><br>### Please provide any relevant code snippet if applicable.<br><br>```shell<br><br>```<br><br>### Code of Conduct<br><br>- [x] I agree to follow this Ax's Code of Conduct</code>                                                                                                                                                                                                                                  | <code>### Question<br><br>Hello,<br><br>Is there a simple way to suppress the following logging message without manually adjusting the class?<br><br>https://github.com/facebook/Ax/blob/main/ax/core/experiment.py#L59<br><br>method: attach_trial()<br><br>        logger.info(<br>            "Attached custom parameterizations "<br>            f"{round_floats_for_logging(item=parameterizations)} "<br>            f"as trial {trial.index}."<br>        )<br><br>Such as using verbose_logging=False to suppress the message of a completed trial.<br><br>Thanks in advance!<br><br>### Please provide any relevant code snippet if applicable.<br><br>```shell<br><br>```<br><br>### Code of Conduct<br><br>- [x] I agree to follow this Ax's Code of Conduct</code>                                                                                                                                                                                                            | <code>1.0</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 4
- `per_device_eval_batch_size`: 4
- `num_train_epochs`: 1
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 4
- `per_device_eval_batch_size`: 4
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 1
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step  | Training Loss |
|:------:|:-----:|:-------------:|
| 0.0178 | 500   | 0.0271        |
| 0.0356 | 1000  | 0.0079        |
| 0.0535 | 1500  | 0.0028        |
| 0.0713 | 2000  | 0.0012        |
| 0.0891 | 2500  | 0.0014        |
| 0.1069 | 3000  | 0.0013        |
| 0.1248 | 3500  | 0.0016        |
| 0.1426 | 4000  | 0.002         |
| 0.1604 | 4500  | 0.0036        |
| 0.1782 | 5000  | 0.0004        |
| 0.1961 | 5500  | 0.0022        |
| 0.2139 | 6000  | 0.0002        |
| 0.2317 | 6500  | 0.0007        |
| 0.2495 | 7000  | 0.0006        |
| 0.2673 | 7500  | 0.0001        |
| 0.2852 | 8000  | 0.0009        |
| 0.3030 | 8500  | 0.0023        |
| 0.3208 | 9000  | 0.0011        |
| 0.3386 | 9500  | 0.0001        |
| 0.3565 | 10000 | 0.0014        |
| 0.3743 | 10500 | 0.0002        |
| 0.3921 | 11000 | 0.0009        |
| 0.4099 | 11500 | 0.0009        |
| 0.4277 | 12000 | 0.0001        |
| 0.4456 | 12500 | 0.0015        |
| 0.4634 | 13000 | 0.0014        |
| 0.4812 | 13500 | 0.0002        |
| 0.4990 | 14000 | 0.0021        |
| 0.5169 | 14500 | 0.0017        |
| 0.5347 | 15000 | 0.0008        |
| 0.5525 | 15500 | 0.0002        |
| 0.5703 | 16000 | 0.0           |
| 0.5882 | 16500 | 0.0014        |
| 0.6060 | 17000 | 0.0001        |
| 0.6238 | 17500 | 0.0           |
| 0.6416 | 18000 | 0.0023        |
| 0.6594 | 18500 | 0.0007        |
| 0.6773 | 19000 | 0.0014        |
| 0.6951 | 19500 | 0.0012        |
| 0.7129 | 20000 | 0.0013        |
| 0.7307 | 20500 | 0.0016        |
| 0.7486 | 21000 | 0.0           |
| 0.7664 | 21500 | 0.0           |
| 0.7842 | 22000 | 0.0009        |
| 0.8020 | 22500 | 0.0007        |
| 0.8198 | 23000 | 0.0001        |
| 0.8377 | 23500 | 0.0001        |
| 0.8555 | 24000 | 0.0009        |
| 0.8733 | 24500 | 0.0           |
| 0.8911 | 25000 | 0.0           |
| 0.9090 | 25500 | 0.0014        |
| 0.9268 | 26000 | 0.0023        |
| 0.9446 | 26500 | 0.0008        |
| 0.9624 | 27000 | 0.0006        |
| 0.9803 | 27500 | 0.0001        |
| 0.9981 | 28000 | 0.0           |


### Framework Versions
- Python: 3.11.14
- Sentence Transformers: 5.2.0
- Transformers: 4.57.3
- PyTorch: 2.9.1+cu128
- Accelerate: 1.12.0
- Datasets: 4.4.2
- Tokenizers: 0.22.2

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{henderson2017efficient,
    title={Efficient Natural Language Response Suggestion for Smart Reply},
    author={Matthew Henderson and Rami Al-Rfou and Brian Strope and Yun-hsuan Sung and Laszlo Lukacs and Ruiqi Guo and Sanjiv Kumar and Balint Miklos and Ray Kurzweil},
    year={2017},
    eprint={1705.00652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->