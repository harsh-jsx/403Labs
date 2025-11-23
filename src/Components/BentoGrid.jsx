// simple className combiner
function cn(...classes) {
  return classes.filter(Boolean).join(" ");
}

// simple arrow icon (replacing @radix-ui/react-icons)
const ArrowRightIcon = ({ className }) => (
  <svg
    className={className}
    width="16"
    height="16"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    viewBox="0 0 24 24"
  >
    <path d="M5 12h14M13 6l6 6-6 6" />
  </svg>
);

// simple button replacing shadcn/ui <Button>
const Button = ({ children, className, ...props }) => (
  <button
    className={cn(
      "text-blue-600 hover:underline inline-flex items-center gap-1",
      className
    )}
    {...props}
  >
    {children}
  </button>
);

export const BentoGrid = ({ children, className, ...props }) => {
  return (
    <div
      className={cn(
        "grid w-full auto-rows-[22rem] grid-cols-3 gap-4",
        className
      )}
      {...props}
    >
      {children}
    </div>
  );
};

export const BentoCard = ({
  name,
  className,
  background,
  Icon,
  description,
  href,
  cta,
  ...props
}) => (
  <div
    className={cn(
      "group relative col-span-3 flex flex-col justify-between overflow-hidden rounded-xl",
      "bg-white shadow-[0_0_0_1px_rgba(0,0,0,.03),0_2px_4px_rgba(0,0,0,.05),0_12px_24px_rgba(0,0,0,.05)]",
      className
    )}
    {...props}
  >
    <div>{background}</div>

    <div className="p-4">
      <div className="pointer-events-none z-10 flex transform-gpu flex-col gap-1 transition-all duration-300 lg:group-hover:-translate-y-10">
        {Icon && (
          <Icon className="h-12 w-12 origin-left transform-gpu text-neutral-700 transition-all duration-300 ease-in-out group-hover:scale-75" />
        )}

        <h3 className="text-xl font-semibold text-neutral-700">{name}</h3>

        <p className="max-w-lg text-neutral-500">{description}</p>
      </div>

      <div className="pointer-events-none flex w-full translate-y-0 transform-gpu flex-row items-center transition-all duration-300 lg:hidden">
        <Button className="pointer-events-auto p-0">
          <a href={href} className="flex items-center">
            {cta}
            <ArrowRightIcon className="ms-2 h-4 w-4" />
          </a>
        </Button>
      </div>
    </div>

    <div className="pointer-events-none absolute bottom-0 hidden w-full translate-y-10 transform-gpu flex-row items-center p-4 opacity-0 transition-all duration-300 group-hover:translate-y-0 group-hover:opacity-100 lg:flex">
      <Button className="pointer-events-auto p-0">
        <a href={href} className="flex items-center">
          {cta}
          <ArrowRightIcon className="ms-2 h-4 w-4" />
        </a>
      </Button>
    </div>

    <div className="pointer-events-none absolute inset-0 transform-gpu transition-all duration-300 group-hover:bg-black/[.03]" />
  </div>
);
